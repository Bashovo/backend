from myapi.schema import schema
from django.urls import include, path
from rest_framework import routers
from . import views
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
# router = routers.DefaultRouter()
# router.register(r'songs', views.SongViewSet)
# router.register(r'albums', views.AlbumViewSet)

urlpatterns = [
     path("", csrf_exempt(GraphQLView.as_view(graphiql=True,schema=schema))),

]