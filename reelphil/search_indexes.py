from haystack.indexes import *
from haystack import site
from movie.models import Movie, ItemList
from django.contrib.auth.models import User


class MovieIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        "Used when the entire index for model is updated."
        return Movie.objects.all()

site.register(Movie, MovieIndex)


class ListIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        "Used when the entire index for model is updated."
        return ItemList.objects.all()

site.register(ItemList, ListIndex)


class UserIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def index_queryset(self):
        "Used when the entire index for model is updated."
        return User.objects.all()

site.register(User, UserIndex)
