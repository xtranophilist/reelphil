from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from users import views as users_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from movie.api import MovieResource

v1_api = Api(api_name='v1')
v1_api.register(MovieResource())
# v1_api.register(EntryResource())

urlpatterns = patterns('',
    url(r'^social/', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('users.urls')),
    (r'^profiles/', include('profiles.urls')),
    url(r'^api/', include(v1_api.urls)),
    url('^$',  include('home.urls')),
    url(r'', include('movie.urls')),

    )

urlpatterns += staticfiles_urlpatterns()
