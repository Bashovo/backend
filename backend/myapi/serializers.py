from rest_framework import serializers

from .models import Song,Album

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('id','title')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    songs = serializers.StringRelatedField(many=True,read_only=True)
     
    class Meta:
        model = Album
        fields = ('id','albumName','artist','songs')