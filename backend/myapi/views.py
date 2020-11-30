from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import SongSerializer,AlbumSerializer
from .models import Album,Song


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('title')
    serializer_class = SongSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('albumName')
    serializer_class = AlbumSerializer