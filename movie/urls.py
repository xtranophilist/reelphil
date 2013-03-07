from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^movie/(?P<slug>[a-zA-Z0-9_.-]+)$', 'movie.views.movie'),
                       url(r'^person/(?P<slug>[a-zA-Z0-9_.-]+)$', 'movie.views.person'),
                       url(r'^list/(?P<slug>[a-zA-Z0-9_.-]+)$', 'movie.views.item_list'),
                       )
