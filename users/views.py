from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from users.models import Profile
from users.forms import ProfileForm
from django.http import Http404
from django.http import HttpResponseRedirect
from users.serializers import ProfileSerializer
from movie.serializers import ActivitySerializer
from movie.models import Activity


def web_login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect('/', **kwargs)
    else:
        return login(request, **kwargs)


def profile(request, username=None):
    if username:
        try:
            web_user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
    else:
        web_user = request.user
    try:
        profile = Profile.objects.get(user=web_user)
    except Profile.DoesNotExist:
        raise Http404
    profile_data = ProfileSerializer(profile).data
    obj = Activity.objects.filter(user=web_user).order_by('-id')[:10]
    timeline = ActivitySerializer(obj).data
    return render(request, 'profiles/profile_detail.html', {"web_user": web_user, "profile": profile_data, 'timeline': timeline})


def edit_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, files=request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/edit_profile.html', {"profile": profile, "form": ProfileForm})
