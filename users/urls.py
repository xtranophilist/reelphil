from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^registration_success/$', views.registration_success, name='registration_success'),
    # url(r'^$', views.logout, name='logout'),
    # url(r'^$', views., name='login'),

)