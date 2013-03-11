from django.shortcuts import render
from models import Movie, Person
# from tastypie.serializers import Serializer
# from movie.api import ListResource
from reelphil.helper import serialize

from rest_framework import generics
from movie.serializers import MovieSerializer, ListSerializer


def movie(request, slug):
    # movie = Movie.objzects.get(slug=slug)
    # print type(movie)
    return render(request, 'movie/movie.html', {"movie": serialize(MovieSerializer, slug=slug)})


def all_movies(request):
    return render(request, 'movie/all_movies.html', {"movies": serialize(MovieSerializer)})


def person(request, slug):
    person = Person.objects.get(slug=slug)
    return render(request, 'movie/person.html', {"person": person})


def item_list(request, slug):
    return render(request, 'movie/list.html', {"item_list": serialize(ListSerializer, slug=slug)})


class MovieList(generics.ListCreateAPIView):
    model = Movie
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Movie
    serializer_class = MovieSerializer
