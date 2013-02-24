from django.conf.urls import patterns, include, url
from users import views as users_views

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
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^login/$', users_views.login_user, name='login'),
    url(r'^logout/$', users_views.logout_user, name='logout'),
    url(r'^register/$', users_views.register_user, name='register'),
    # (r'^login/?$', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}),
    url('^$',  include('home.urls')),
    url(r'^movies/', include('movies.urls')),
    )
