from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from models import Movie


@login_required
def index(request):
    return render(request, 'movies/all.html', {"movie": movie})


def movie(request):
    slug = request.path.replace('/movies/', '')
    movie = Movie.objects.get(slug=slug)
    print movie.id
    return render(request, 'movies/movie.html', {"movie": movie})


# def list(request):
#     ia = IMDb('sql', uri='mysql://root:passweird@localhost/reelphil')
#     # ia = IMDb()
#     list = ia.get_top250_movies()
#     return render(request, 'movies/list.html', {"list": list})
