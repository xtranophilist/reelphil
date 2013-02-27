from django.conf.urls import patterns, include, url
from registration.views import register
from users.registrationform import UserRegistrationForm

urlpatterns = patterns('',
    url(r'^register/$', register, {'backend': 'registration.backends.simple.SimpleBackend', 'form_class': UserRegistrationForm}, name='registration_register'),
    url(r'^register/$', register, {'backend': 'registration.backends.default.DefaultBackend', 'form_class': UserRegistrationForm}, name='registration_register'),
    (r'^', include('registration.backends.simple.urls')),
 # url(r'^login/$', users_views.login_user, name='login'),
 # url(r'^logout/$', users_views.logout_user, name='logout'),
 # url(r'^register/$', users_views.register_user, name='register'),
 # (r'^login/?$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),
 )
