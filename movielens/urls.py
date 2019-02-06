from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('user/<int:userid>/', views.user_page),
    path('user/<int:userid>/browse', views.user_browse),
    path('user/<int:userid>/movie/<int:movieid>/', views.user_view_movie),
]