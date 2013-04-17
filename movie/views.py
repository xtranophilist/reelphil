from django.shortcuts import render
from models import Movie, Person, ItemList, Activity, ListUser
# from tastypie.serializers import Serializer
# from movie.api import ListResource
from reelphil.helper import serialize
from django.contrib.auth.models import User

from rest_framework import generics
from movie.serializers import FullMovieSerializer, FullListSerializer, FullPersonSerializer, ListSerializer


def movie(request, slug):
    the_movie = FullMovieSerializer(Movie.objects.get(slug=slug)).data
    return render(request, 'movie.html', {"movie": the_movie})


def all_movies(request):
    return render(request, 'movies.html', {"movies": serialize(FullMovieSerializer)})


def person(request, slug):
    person = FullPersonSerializer(Person.objects.get(slug=slug)).data
    return render(request, 'person.html', {"person": person})


def item_list(request, slug):
    the_list = FullListSerializer(ItemList.objects.get(slug=slug)).data
    return render(request, 'list.html', {"item_list": the_list})


def all_lists(request):
    return render(request, 'lists.html', {"lists": serialize(ListSerializer), "header": "All Lists"})


def movies(request, activity_type, user=None):
    if user is None:
        usr = request.user
    else:
        usr = User.objects.get(username=user)
    watches = Activity.objects.filter(user=usr, activity_type=activity_type).select_related(depth=1)
    movies = [activity.movie for activity in watches]
    print movies
    # obj = Movie.objects.filter()
    movies = FullMovieSerializer(movies).data
    header = 'All Movies ' + {1: 'Owned', 2: 'Watched', 3: 'Liked', 4: 'Disliked', 5: 'Favorited'}[activity_type] + ' by ' + unicode(usr)
    return render(request, 'movies.html', {"movies": movies, "header": header})


def favorited_lists(request, user=None):
    if user is None:
        usr = request.user
    else:
        usr = User.objects.get(username=user)
    list_user = ListUser.objects.filter(user=usr, favorited=True).select_related(depth=1)
    lists = [lu.item_list for lu in list_user]
    lists_data = ListSerializer(lists).data
    return render(request, 'lists.html', {"lists": lists_data, "header": "All Favorited Lists"})


def on_watchlist_lists(request, user=None):
    if user is None:
        usr = request.user
    else:
        usr = User.objects.get(username=user)
    list_user = ListUser.objects.filter(user=usr, on_watchlist=True).select_related(depth=1)
    lists = [lu.item_list for lu in list_user]
    lists_data = ListSerializer(lists).data
    return render(request, 'lists.html', {"lists": lists_data, "header": "All Watchlists"})


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
