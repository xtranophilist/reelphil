from django.conf.urls import patterns, url, include

from rest_framework.urlpatterns import format_suffix_patterns
from movie.views import MovieList, MovieDetail

urlpatterns = patterns('',
                       url(r'^$', 'api_root'),
                       url(r'^api/movies/$', MovieList.as_view(), name='movie-list'),
                       url(r'^api/movie/(?P<slug>[a-zA-Z0-9_.-]+)/$', MovieDetail.as_view(), name='movie-detail'),
                       url(r'^movies/$', 'movie.views.all_movies'),
                       url(r'^movie/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'movie.views.movie'),
                       url(r'^person/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'movie.views.person'),
                       url(r'^list/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'movie.views.item_list'),
                       )

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
                        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
                        )
