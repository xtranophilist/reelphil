from django.shortcuts import render
from models import Movie


def movie(request):
    slug = request.path.replace('/movie/', '')
    movie = Movie.objects.get(slug=slug)
    return render(request, 'movie/movie.html', {"movie": movie})


# def list(request):
#     ia = IMDb('sql', uri='mysql://root:passweird@localhost/reelphil')
#     # ia = IMDb()
#     list = ia.get_top250_movies()
#     return render(request, 'movies/list.html', {"list": list})
