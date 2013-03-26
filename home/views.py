from django.shortcuts import render
from movie.models import Activity
from movie.serializers import ActivitySerializer
from users.models import Profile
from django.db.models import Q


def index(request):
    profile = Profile.objects.get(user=request.user)
    following = [prof.user for prof in profile.following.all()]
    obj = Activity.objects.filter(Q(user__in=following) | Q(user=request.user)).order_by('-id')[:10]
    timeline = ActivitySerializer(obj).data
    return render(request, 'home.html', {'timeline': timeline})
