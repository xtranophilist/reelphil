from django.shortcuts import render
from movie.models import Activity
from movie.serializers import ActivitySerializer
from django.db.models import Q
# from django.db.models.aggregates import Max


def do_filter(activities):
    ret = []
    for activity in activities:
        if activity.activity_type is 2 and any(a.timestamp == activity.timestamp and a.activity_type is 6 for a in ret):
            pass
        else:
            print activity.timestamp, activity.activity_type
            ret.append(activity)
    return ret


def index(request):
    if request.user.is_authenticated():
        followings = [following.user for following in request.user.get_profile().following.all()]
        activities = Activity.objects.filter(Q(user__in=followings) | Q(user=request.user)).order_by('-timestamp', '-activity_type')
    else:
        activities = Activity.objects.all().order_by('-id')
    activities = do_filter(activities)
    timeline = ActivitySerializer(activities).data
    return render(request, 'home.html', {'timeline': timeline})
