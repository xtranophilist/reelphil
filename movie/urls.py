from django.conf.urls import patterns, url
from movie import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'', views.movie, name='movie')
    )
