from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
import boto3

from django.conf import settings

from .models import Item
from .models import User
from .models import UserData
from .models import Poster

POSTER_LOCATION = "/Users/chris/projects/personalens/data/ml-100k/movie_poster.csv"
personalize_runtime = boto3.client(service_name='personalize-runtime', endpoint_url='https://personalize-runtime.us-east-1.amazonaws.com')
campaign_arn = "arn:aws:personalize:us-east-1:059124553121:campaign/Django-campaign"


def get_recommendations(user_id):
    """

    :param user_id:
    :return:
    """
    get_recommendations_response = personalize_runtime.get_recommendations(
        campaignArn=campaign_arn,
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

    :param request:
    :param userid:
    :return:
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

        :param request:
        :param userid:
        :return:
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

    :param user:
    :param movie:
    :return:
    """
    # TODO CLICK EVENT GOES HERE
    print("Clickstream Status: ", str(settings.STREAM_EVENTS))
    if settings.STREAM_EVENTS:
        print("Streaming event: ", str(user), str(movie))
    else:
        print("Not streaming events")

def user_view_movie(request, userid, movieid):
    """

        :param request:
        :param userid:
        :param movieid
        :return:
        """
    user = User.objects.get(user_id=userid)
    movie = Item.objects.get(movie_id=movieid)
    stream_event(user, movie)

    return redirect(movie.IMDB_URL)


