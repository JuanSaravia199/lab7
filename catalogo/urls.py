from django.urls import path
from . import views

urlpatterns = [
    path("animes/", views.anime_list, name="anime-list"),
]