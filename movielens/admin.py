from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User
from .models import Item
from .models import UserData
from .models import Poster

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'age', 'gender', 'occupation', 'zip_code')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'movie_title', 'release_date', 'video_release_date', 'IMDB_URL',
          'unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime',
          'Documentary', 'Drama', 'Fantasy', 'Film_Noir', 'Horror', 'Musical', 'Mystery',
          'Romance', 'Sci_Fi', 'Thriller', 'War', 'Western')


class UserDataAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'item_id', 'rating', 'timestamp')


class PosterAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'filename')

admin.site.register(User, UserAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(UserData, UserDataAdmin)
admin.site.register(Poster, PosterAdmin)
