import graphene
from graphene_django import DjangoObjectType
from .models import Album,Song

# Create a GraphQL type for the actor model
class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        

# Create a GraphQL type for the movie model
class SongType(DjangoObjectType):
    class Meta:
        model = Song
        fields = ("id", "title")

class Query(graphene.ObjectType):
    song = graphene.Field(SongType, id=graphene.Int())
    album = graphene.Field(AlbumType, id=graphene.Int())
    songs = graphene.List(SongType)
    albums= graphene.List(AlbumType)

    def resolve_song(self, info, **kwargs):
        id = kwargs.get('id')
        all
        if id is not None:
            return Song.objects.get(pk=id)
        return None

    def resolve_album(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Album.objects.get(pk=id)

        return None

    def resolve_songs(root, info):
        return Song.objects.all()

    def resolve_albums(root, info):
        return Album.objects.all()


schema = graphene.Schema(query=Query)

