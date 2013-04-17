from django.conf.urls import patterns, url, include

from rest_framework.urlpatterns import format_suffix_patterns
from movie.views import MovieList, MovieDetail

urlpatterns = patterns('',
                       url(r'^$', 'api_root'),
                       url(r'^api/movies/$', MovieList.as_view(), name='movie-list'),
                       url(r'^api/movie/(?P<slug>[a-zA-Z0-9_.-]+)/$', MovieDetail.as_view(), name='movie-detail'),
                       url(r'^movies/$', 'movie.views.all_movies'),
                       url(r'^movies/owned/$', 'movie.views.movies', {'activity_type': 1}),
                       url(r'^movies/owned/(?P<user>[a-zA-Z0-9_.-]+)/$', 'movie.views.movies', {'activity_type': 1}),
                       url(r'^movies/watched/$', 'movie.views.movies', {'activity_type': 2}),
                       url(r'^movies/watched/(?P<user>[a-zA-Z0-9_.-]+)/$', 'movie.views.movies', {'activity_type': 2}),
                       url(r'^movies/liked/$', 'movie.views.movies', {'activity_type': 3}),
                       url(r'^movies/liked/(?P<user>[a-zA-Z0-9_.-]+)/$', 'movie.views.movies', {'activity_type': 3}),
                       url(r'^movies/disliked/$', 'movie.views.movies', {'activity_type': 4}),
                       url(r'^movies/disliked/(?P<user>[a-zA-Z0-9_.-]+)/$', 'movie.views.movies', {'activity_type': 4}),
                       url(r'^movies/favorited/$', 'movie.views.movies', {'activity_type': 5}),
                       url(r'^movies/favorited/(?P<user>[a-zA-Z0-9_.-]+)/$', 'movie.views.movies', {'activity_type': 5}),
                       url(r'^movie/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'movie.views.movie'),
                       url(r'^person/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'movie.views.person'),
                       url(r'^lists/$', 'movie.views.all_lists'),
                       url(r'^lists/favorited/$', 'movie.views.favorited_lists'),
                       url(r'^lists/favorited/(?P<user>[a-zA-Z0-9_.-]+)/$', 'movie.views.favorited_lists'),
                       url(r'^lists/on_watchlist/$', 'movie.views.on_watchlist_lists'),
                       url(r'^lists/on_watchlist/(?P<user>[a-zA-Z0-9_.-]+)/$', 'movie.views.on_watchlist_lists'),
                       url(r'^list/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'movie.views.item_list'),
                       )

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
                        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
                        )
