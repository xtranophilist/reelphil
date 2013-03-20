from django.shortcuts import render, redirect
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from users.models import Profile


def web_login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect('/', **kwargs)
    else:
        return login(request, **kwargs)


def profile(request, username=None):
    if username:
        web_user = User.objects.get(username=username)
    else:
        web_user = request.user
    profile = Profile.objects.get(user=web_user)
    print profile.checkins
    return render(request, 'profiles/profile_detail.html', {"web_user": web_user})


def edit_profile(request):
    return render(request, 'profiles/edit_profile.html', {"web_user": profile})
