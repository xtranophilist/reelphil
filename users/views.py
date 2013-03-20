from django.shortcuts import render, redirect
from django.contrib.auth.views import login


def web_login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect('/', **kwargs)
    else:
        return login(request, **kwargs)


def profile(request):
    return render(request, 'profiles/profile_detail.html', {"profile": profile})
