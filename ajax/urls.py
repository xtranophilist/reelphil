from django.conf.urls import patterns, url

# from ajax.views import Generic

urlpatterns = patterns('',
                        url(r'^movie/$', 'ajax.views.movie'),
                        url(r'^(?P<model>[a-z]+)/$', 'ajax.views.generic_handler'),
                       )
