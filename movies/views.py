from django.shortcuts import render
from imdb import IMDb


def index(request):
    ia = IMDb('sql', uri='mysql://root:passweird@localhost/reelphil')
    movie = ia.get_movie('1318514')
    print movie['title']
    return render(request, 'movies/movie.html', {"movie": movie})


def list(request):
    ia = IMDb('sql', uri='mysql://root:passweird@localhost/reelphil')
    # ia = IMDb()
    list = ia.get_top250_movies()
    return render(request, 'movies/list.html', {"list": list})
