from django.shortcuts import render
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('posts', views.posts_page_view, name='posts'),
    path('games', views.games_page_view, name='games'),
]