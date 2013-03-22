from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.utils import simplejson
from django.template import Library
from django.utils.safestring import mark_safe
from movie.models import Checkin, Activity

register = Library()


@register.filter
def jsonify(object):
    if isinstance(object, QuerySet):
        return serialize('json', object)
    return mark_safe(simplejson.dumps(object))


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_recent_checkins(user, num=5):
    checkins = Checkin.objects.filter(user=user).order_by('-id')[:num]
    return checkins


@register.filter
def get_activity(type):
    return {1: 'owned', 2: 'watched', 3: 'liked', 4: 'disliked', 5: 'favorited'}[type]


@register.filter
def get_recent_activity(user, num=5):
    activities = Activity.objects.filter(user=user).order_by('-id')[:num]
    all_activities = []
    for activity in activities:
        act = {1: 'owned', 2: 'watched', 3: 'liked', 4: 'disliked', 5: 'favorited'}[activity.activity_type]
        time = activity.timestamp
        item = activity.movie
        all_activities.append([act, item, time])
    checkins = Checkin.objects.filter(user=user).order_by('-id')[:num]
    for checkin in checkins:
        act = 'checked-in to'
        time = checkin.checktime
        item = checkin.movie
        all_activities.append([act, item, time])
    return all_activities
