from django.conf.urls import patterns, url
from item_list import views

urlpatterns = patterns('',
    url(r'', views.list, name='list')
    )
