from django.shortcuts import render
from models import Movie, Person
# from tastypie.serializers import Serializer
from movie.api import ListResource


def movie(request, slug):
    movie = Movie.objects.get(slug=slug)
    return render(request, 'movie/movie.html', {"movie": movie})


def person(request, slug):
    person = Person.objects.get(slug=slug)
    return render(request, 'movie/person.html', {"person": person})


def item_list(request, slug):
    # item_list = ItemList.objects.get(slug=slug)
    # # serializer = Serializer()
    # # serializer
    # # print serializer.serialize(item_list)
    # lr = ListResource()
    # item_list = lr.obj_get(request=request, slug=slug)
    # lr_bundle = lr.build_bundle(obj=item_list, request=request)
    # return render(request, 'movie/list.html', {"item_list": lr.serialize(None, lr.full_dehydrate(lr_bundle), 'application/json')})
    # return render(request, 'movie/list.html', {"item_list": item_list})
    lr = ListResource()
    return render(request, 'movie/list.html', {"item_list": resource_to_json(lr)})


def resource_to_json(resource):
    r_list = resource.get_object_list(None)
    r_to_serialize = [resource.full_dehydrate(resource.build_bundle(obj=obj)) for obj in r_list]
    return resource.serialize(None, r_to_serialize, 'application/json')

