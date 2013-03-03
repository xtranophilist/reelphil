from django.conf.urls import patterns, include, url

# from users import views as users_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reelphil.views.home', name='home'),
    # url(r'^reelphil/', include('reelphil.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^social/', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^$',  include('home.urls')),
    url(r'^user/', include('users.urls')),
    (r'^profiles/', include('profiles.urls')),
    url(r'^movie/', include('movie.urls')),
    url(r'^person/', include('person.urls')),
    url(r'^list/', include('list.urls')),
    )
