from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
import boto3

from django.conf import settings

from .models import Item
from .models import User
from .models import UserData
from .models import Poster


# Establish a connection for all views to use.


def get_recommendations(user_id):
    """
    get_recommendations takes in a user_id, queries it against the active campaign to return
    a list of Item(Movie) objects to be rendered on a page.
    :param user_id: passed in as an int, but refers to a userId inside the solution.
    :return: list of movies to be rendered.
    """

    # Establish boto connection:
    personalize_runtime = boto3.client(service_name='personalize-runtime',
                                       endpoint_url='https://personalize-runtime.us-east-1.amazonaws.com')

    get_recommendations_response = personalize_runtime.get_recommendations(
        campaignArn=settings.CAMPAIGN_ARN,
        userId=str(user_id),
    )
    item_list = get_recommendations_response['itemList']
    items_to_return = []
    for item in item_list:
        movie = Item.objects.get(movie_id=item['itemId'])
        movie.poster = Poster.objects.get(item=movie)
        items_to_return.append(movie)
    return items_to_return


def index(request):
    """
    This function is responsible for the application's homepage. Simply returns a HTTP response listing
    all users and links to explore them within the application.
    :param request: standard HTTP get request.
    :return: Main application page.
    """
    users = User.objects.all()
    for user in users:
        user.reviews = UserData.objects.filter(user_id=user).count()
    context = {
        'request': request,
        'users': users,
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def user_page(request, userid):
    """
    user_page returns a page showcasing the metadata of the user, a collection of recommendations
    and their reviews.
    :param request: standard HTTP get request
    :param userid: int value representing a user in the campaign and database
    :return: HTML page showcasing user info described above.
    """
    user = User.objects.get(user_id=userid)
    recommendations = get_recommendations(user_id=userid)
    reviews = UserData.objects.filter(user_id=user)
    context = {
        'ml_user': user,
        'request': request,
        'reviews': reviews,
        'recommendations': recommendations,
    }
    template = loader.get_template('user_index.html')
    return HttpResponse(template.render(context, request))


def user_browse(request, userid):
    """
    user_browse renders a collection of random movies for a user to click or not, thus
    updating recommendations.
    :param request: standard HTTP get request
    :param userid: int value representing a user in the campaign and database
    :return: HTML page with a collection of random movies to browse
    """
    user = User.objects.get(user_id=userid)
    movies = Item.objects.all().order_by('?')[:20]
    for movie in movies:
        movie.poster = Poster.objects.get(item=movie)
    context = {
        'ml_user': user,
        'request': request,
        'movies' : movies,
    }
    template = loader.get_template('user_browse.html')
    return HttpResponse(template.render(context, request))


def stream_event(user, movie):
    """
    stream_event takes in a user object as well as a item/movie and sends the data out
    as a click stream event to the campaign. This combined with the user's active
    session will alter the recommendations displayed.
    :param user: User object
    :param movie: Item object
    :return: None
    """
    # TODO CLICK EVENT GOES HERE
    print("Clickstream Status: ", str(settings.STREAM_EVENTS))
    if settings.STREAM_EVENTS:
        print("Streaming event: ", str(user), str(movie))
    else:
        print("Not streaming events")


def user_view_movie(request, userid, movieid):
    """
    user_view_movie handles allowing the app to capture a click, processing it, then
    redirecting the user to IMDB for more information on the Movie.
    :param request: standard HTTP get request
    :param userid: int value representing a user in the campaign and database
    :param movieid: int value representing a item in the campaign and database
    :return: returns an HTTP redirect to IMDB
    """
    user = User.objects.get(user_id=userid)
    movie = Item.objects.get(movie_id=movieid)
    stream_event(user, movie)
    return redirect(movie.IMDB_URL)
