from django.shortcuts import render
from models import Person


def person(request):
    slug = request.path.replace('/person/', '')
    person = Person.objects.get(slug=slug)
    # print movie.direction_set.all()
    return render(request, 'person/person.html', {"person": person})
