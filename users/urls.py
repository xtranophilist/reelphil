from django.conf.urls import patterns, include, url
from registration.views import register
from users.forms import UserRegistrationForm
from users.views import web_login

urlpatterns = patterns('',
    url(r'^login/$', web_login, {'template_name': 'registration/login.html'}, name='auth_login'),
    # url(r'^register/$', register, {'backend': 'registration.backends.simple.SimpleBackend', 'form_class': UserRegistrationForm}, name='registration_register'),
    url(r'^register/$', register, {'backend': 'registration.backends.default.DefaultBackend', 'form_class': UserRegistrationForm}, name='registration_register'),
    url(r'^$', 'users.views.profile'),
    url(r'^edit/$', 'users.views.edit_profile'),
    url(r'^auth-error/$', 'users.views.auth_error'),
    (r'^', include('registration.backends.default.urls')),
    url(r'^(?P<username>[a-zA-Z0-9_.-]+)/$', 'users.views.profile', name='user-detail'),
 # url(r'^login/$', users_views.login_user, name='login'),
 # url(r'^logout/$', users_views.logout_user, name='logout'),
 # url(r'^register/$', users_views.register_user, name='register'),
 # (r'^login/?$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),
 )
