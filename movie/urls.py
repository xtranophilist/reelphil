from django.conf.urls import patterns, url
from django.conf.urls.defaults import include
from movie import views

urlpatterns = patterns('',
    # url(r'^ajax/', views.ajax, name='ajax'),
    url(r'^(?P<slug>[a-zA-Z0-9_.-]+)', views.movie, name='movie'),
    )
