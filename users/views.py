from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from users.forms import RegistrationForm
# from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def login_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    state = 'Please enter your username and password:'
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                state = 'Your account is not yet activated!'
        else:
            state = 'Incorrect username/password!'

    return render(request, 'users/login.html', {'username': username, 'password': password, 'state': state})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def registration_success(request):
    return render(request, 'users/registration_success.html', {
        # 'address': email
        })


def register_user(request):
    logout(request)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(
            #     cd.get('subject'),
            #     cd.get('message'),
            #     cd.get('email', 'noreply@example.com'),
            #     ['siteowner@example.com'],
            # )
            user = User.objects.create_user(cd.get('username'), cd.get('email'), make_password(cd.get('password')))
            user.is_active = False
            user.save()
            return HttpResponseRedirect('/users/registration_success/')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})
