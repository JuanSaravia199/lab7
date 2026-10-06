from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Anime
from .serializers import AnimeSerializer

# 1. Vista de lista y creación con @api_view (Semana 8)
@api_view(['GET', 'POST'])
def anime_lista(request):
    if request.method == 'GET':
        animes = Anime.objects.all()
        serializer = AnimeSerializer(animes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 2. Vista de detalle y edición con APIView (Semana 8)
class AnimeDetalle(APIView):
    def get(self, request, pk):
        anime = get_object_or_404(Anime, pk=pk)
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)

    def put(self, request, pk):
        anime = get_object_or_404(Anime, pk=pk)
        serializer = AnimeSerializer(anime, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)