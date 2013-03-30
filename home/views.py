from django.shortcuts import render
from movie.models import Activity
from movie.serializers import ActivitySerializer
from django.db.models import Q
from django.db.models.aggregates import Max


def filterDuplicate(activity, activities):
    # print type(activity.timestamp)
    # print activities.values('timestamp')
    print activity
    items = [item.get('timestamp') for item in activities.values('timestamp')]
    print activity.timestamp in items

    return True


def index(request):
    if request.user.is_authenticated():
        # TODO single db query http://stackoverflow.com/questions/8825249/django-selecting-distinct-field-not-working
        followings = [following.user for following in request.user.get_profile().following.all()]
        activities = Activity.objects.filter(Q(user__in=followings) | Q(user=request.user)).distinct().order_by('-id')[:10]
        # print activities
    else:
        activities = Activity.objects.all().order_by('-id').annotate(activity_type=Max('activity_type'))
    # activities = Activity.objects.all().values('timestamp', 'user_id', 'movie_id').annotate(activity_t=Max('activity_type'))
    print activities
    # print Activity.objects.values_list('timestamp', flat=True).distinct()
    # activities = [activity for activity in activities if filterDuplicate(activity, activities)]
    timeline = ActivitySerializer(activities).data
    return render(request, 'home.html', {'timeline': timeline})
