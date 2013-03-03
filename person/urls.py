from django.conf.urls import patterns, url
from person import views

urlpatterns = patterns('',
    # url(r'^$', views.index, name='index'),
    url(r'', views.person, name='person')
    )
