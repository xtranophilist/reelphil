from django.views.decorators.csrf import csrf_exempt
from movie.models import *
from django.utils import simplejson
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


def json_response(something):
    return HttpResponse(simplejson.dumps(something))


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


# @csrf_exempt
# def generic_handler(request, model):
#     if request.method == 'POST':
#         model_name = model.capitalize()
#         model_item = eval(model_name).objects.get(id=request.POST['id'])


@csrf_exempt
def movie(request):
    if request.method == 'POST':
        try:
            movie = Movie.objects.get(id=request.POST['id'])
            mu = MovieUser.objects.get(movie=movie, user=request.user)
        except ObjectDoesNotExist:
            mu = MovieUser(user=request.user)
            mu.movie_id = request.POST['id']
        value = request.POST['value']
        attribute = getattr(mu, request.POST['attr'])
        if type(attribute) is bool:
            value = str2bool(value)
        setattr(mu, request.POST['attr'], value)
        mu.save()
        return json_response({'result': 'success'})

@csrf_exempt
def checkin(request):
    if request.method == 'POST':
        movie = Movie.objects.get(id=request.POST['id'])
        movie.checkin()

        # try:
        #     movie = Movie.objects.get(id=request.POST['id'])
        #     mu = MovieUser.objects.get(movie=movie, user=request.user)
        # except ObjectDoesNotExist:
        #     mu = MovieUser(user=request.user)
        #     mu.movie_id = request.POST['id']
        # value = request.POST['value']
        # attribute = getattr(mu, request.POST['attr'])
        # if type(attribute) is bool:
        #     value = str2bool(value)
        # setattr(mu, request.POST['attr'], value)
        # mu.save()
        return json_response({'result': 'success'})
