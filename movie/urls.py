from django.conf.urls import patterns, url
from movie import views

urlpatterns = patterns('',
    url(r'^ajax/', views.ajax, name='ajax'),
    url(r'', views.movie, name='movie')
    )
