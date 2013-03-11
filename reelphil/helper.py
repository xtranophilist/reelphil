# from rest_framework import serializers
from rest_framework.renderers import JSONRenderer


#tastypie resource to json
def resource_to_json(resource):
    r_list = resource.get_object_list(None)
    r_to_serialize = [resource.full_dehydrate(resource.build_bundle(obj=obj)) for obj in r_list]
    return resource.serialize(None, r_to_serialize, 'application/json')


def serialize(serializer, **kwargs):
    if kwargs:
        obj = serializer.Meta.model.objects.get(**kwargs)
    else:
        obj = serializer.Meta.model.objects.all()
    return serializer(obj).data


def jsonify(serializer, **kwargs):
    return JSONRenderer().render(serialize(serializer, **kwargs))
