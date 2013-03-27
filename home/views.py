from django.shortcuts import render
from movie.models import Activity
from movie.serializers import ActivitySerializer
from django.db.models import Q


def index(request):
    if request.user.is_authenticated():
        followings = [following.user for following in request.user.get_profile().following.all()]
        obj = Activity.objects.filter(Q(user__in=followings) | Q(user=request.user)).order_by('-id')[:10]
    else:
        obj = Activity.objects.all().order_by('-id')[:10]
    timeline = ActivitySerializer(obj).data
    return render(request, 'home.html', {'timeline': timeline})
