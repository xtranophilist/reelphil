from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.utils import simplejson
from django.template import Library
from django.utils.safestring import mark_safe
from movie.models import Checkin, Activity
from django.db.models import Model
# from django.forms.models import model_to_dict

register = Library()


@register.filter
def jsonify(object):
    if isinstance(object, QuerySet):
        return serialize('json', object)
    if isinstance(object, Model):
        return mark_safe(serialize('json', [object, ]))
    return mark_safe(simplejson.dumps(object))


@register.filter
def user_to_json(user):
    if hasattr(user, '_wrapped') and hasattr(user, '_setup'):
            if user._wrapped.__class__ == object:
                user._setup()
            user = user._wrapped
    user_dict = {'id': user.id, 'username': user.username}
    return mark_safe(simplejson.dumps(user_dict))


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
