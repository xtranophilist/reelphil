from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.utils import simplejson
from django.template import Library
from django.utils.safestring import mark_safe

register = Library()


def jsonify(object):
    if isinstance(object, QuerySet):
        return serialize('json', object)
    # print object.values()
    # return serialize("json", [object])
    return mark_safe(simplejson.dumps(object))

register.filter('jsonify', jsonify)
