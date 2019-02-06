from django.db import models
from django.conf import settings

class User(models.Model):
    """
    user id | age | gender | occupation | zip code
    """
    user_id = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    session = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user_id)


class Item(models.Model):
    """
    movie id | movie title | release date | video release date |
                  IMDb URL | unknown | Action | Adventure | Animation |
                  Children's | Comedy | Crime | Documentary | Drama | Fantasy |
                  Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
                  Thriller | War | Western |
    """
    movie_id = models.IntegerField(primary_key=True)
    movie_title = models.CharField(max_length=250)
    release_date = models.CharField(max_length=50)
    video_release_date = models.CharField(max_length=50)
    IMDB_URL = models.CharField(max_length=450)
    unknown = models.IntegerField(default=0)
    Action = models.IntegerField(default=0)
    Adventure = models.IntegerField(default=0)
    Animation = models.IntegerField(default=0)
    Children = models.IntegerField(default=0)
    Comedy = models.IntegerField(default=0)
    Crime = models.IntegerField(default=0)
    Documentary = models.IntegerField(default=0)
    Drama = models.IntegerField(default=0)
    Fantasy = models.IntegerField(default=0)
    Film_Noir = models.IntegerField(default=0)
    Horror = models.IntegerField(default=0)
    Musical = models.IntegerField(default=0)
    Mystery = models.IntegerField(default=0)
    Romance = models.IntegerField(default=0)
    Sci_Fi = models.IntegerField(default=0)
    Thriller = models.IntegerField(default=0)
    War = models.IntegerField(default=0)
    Western = models.IntegerField(default=0)

    def __str__(self):
        return self.movie_title


class UserData(models.Model):
    """
    UserData is a simple class used to represent the data for a MovieLens
    user. See schema below for more information
    user id | item id | rating | timestamp
    """
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    item_id = models.ForeignKey(Item, on_delete=models.PROTECT)
    rating = models.IntegerField()
    timestamp = models.IntegerField()

    def __str__(self):
        return str(self.user_id) + " : " + self.item_id.movie_title


class Poster(models.Model):
    """
    This stores posters of each movie.
    """
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    filename = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY)

