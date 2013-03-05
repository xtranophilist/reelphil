from django.shortcuts import render
from models import ItemList


def list(request):
    slug = request.path.replace('/list/', '')
    item_list = ItemList.objects.get(slug=slug)
    return render(request, 'list/list.html', {"item_list": item_list})
