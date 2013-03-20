from django.shortcuts import render
from models import Movie, Person, ItemList
# from tastypie.serializers import Serializer
# from movie.api import ListResource
from reelphil.helper import serialize

from rest_framework import generics
from movie.serializers import FullMovieSerializer, FullListSerializer, FullPersonSerializer


def movie(request, slug):
    the_movie = FullMovieSerializer(Movie.objects.get(slug=slug), request).data
    return render(request, 'movie.html', {"movie": the_movie})


def all_movies(request):
    return render(request, 'all_movies.html', {"movies": serialize(FullMovieSerializer)})


def person(request, slug):
    person = FullPersonSerializer(Person.objects.get(slug=slug), request).data
    return render(request, 'person.html', {"person": person})


def item_list(request, slug):
    the_list = FullListSerializer(ItemList.objects.get(slug=slug), request).data
    # return render(request, 'movie/list.html', {"item_list": serialize(ListSerializer(request.user), slug=slug)})
    return render(request, 'list.html', {"item_list": the_list})


class MovieList(generics.ListCreateAPIView):
    model = Movie
    serializer_class = FullMovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Movie
    serializer_class = FullMovieSerializer


# def get_fields_and_properties(model, instance):
#     field_names = [f.name for f in model._meta.fields]
#     property_names = [name for name in dir(model) if isinstance(getattr(model, name), property)]
#     return dict((name, getattr(instance, name), for name in field_names + property_names))
