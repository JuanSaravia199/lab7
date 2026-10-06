from django.urls import path
from . import views

urlpatterns = [
    path('animes/', views.anime_lista, name='anime_lista'),
    path('animes/<int:pk>/', views.AnimeDetalle.as_view(), name='anime_detalle'),
]