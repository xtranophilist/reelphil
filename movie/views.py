from django.shortcuts import render
from models import Movie


def movie(request):
    slug = request.path.replace('/movie/', '')
    movie = Movie.objects.get(slug=slug)
    return render(request, 'movie/movie.html', {"movie": movie})


