from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.utils import simplejson
from django.template import Library
from django.utils.safestring import mark_safe
from movie.models import Checkin

register = Library()


def jsonify(object):
    if isinstance(object, QuerySet):
        return serialize('json', object)
    # print object.values()
    # return serialize("json", [object])
    return mark_safe(simplejson.dumps(object))

register.filter('jsonify', jsonify)


def get_recent_checkins(user, num=5):
    checkins = Checkin.objects.filter(user=user).order_by('-id')[:num]
    return checkins
    # print 1

register.filter('get_recent_checkins', get_recent_checkins)
