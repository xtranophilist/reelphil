# from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from django.forms.models import model_to_dict


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


class ModelDiffMixin(object):
    """
    A model mixin that tracks model fields' values and provide some useful api
    to know what fields have been changed.
    """

    def __init__(self, *args, **kwargs):
        super(ModelDiffMixin, self).__init__(*args, **kwargs)
        self.__initial = self._dict

    @property
    def diff(self):
        d1 = self.__initial
        d2 = self._dict
        diffs = [(k, (v, d2[k])) for k, v in d1.items() if v != d2[k]]
        return dict(diffs)

    @property
    def has_changed(self):
        return bool(self.diff)

    @property
    def changed_fields(self):
        return self.diff.keys()

    def get_field_diff(self, field_name):
        """
        Returns a diff for field if it's changed and None otherwise.
        """
        return self.diff.get(field_name, None)

    @property
    def _dict(self):
        return model_to_dict(self, fields=[field.name for field in
                             self._meta.fields])
