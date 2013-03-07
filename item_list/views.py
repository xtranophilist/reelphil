from django.shortcuts import render
from models import ItemList
from django.core import serializers


def list(request):
    slug = request.path.replace('/list/', '')
    item_list = ItemList.objects.get(slug=slug)
    # jsonSerializer = JSONSerializer()

    # return json_response_from(item_list)
    # json_str = jsonSerializer.serialize(item_list.items.all())
    json_str = serializers.serialize('json', item_list.items.all(), indent=4, relations=('directors',), excludes=('pk'), fields=('title', 'slug'))

    # # json = helper.jsonify(item_list.items.all())
    return render(request, 'list/list.html', {"item_list": json_str})
