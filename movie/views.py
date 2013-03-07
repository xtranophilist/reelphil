from django.shortcuts import render
from models import Movie, Person, ItemList


def movie(request, slug):
    movie = Movie.objects.get(slug=slug)
    return render(request, 'movie/movie.html', {"movie": movie})


def person(request, slug):
    person = Person.objects.get(slug=slug)
    return render(request, 'movie/person.html', {"person": person})


def item_list(request, slug):
    item_list = ItemList.objects.get(slug=slug)
    return render(request, 'movie/list.html', {"item_list": item_list})
