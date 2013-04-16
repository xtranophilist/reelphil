from django.conf.urls import patterns, url

# from ajax.views import Generic

urlpatterns = patterns('',
                        url(r'^movie/$', 'ajax.views.movie'),
                        url(r'^movie/checkin/$', 'ajax.views.checkin'),
                        url(r'^listitem/$', 'ajax.views.list_item'),
                        url(r'^listview/$', 'ajax.views.list_item'),
                        url(r'^follow/$', 'ajax.views.follow'),
                        url(r'^unfollow/$', 'ajax.views.unfollow'),
                        url(r'^delete/$', 'ajax.views.delete'),
                        # url(r'^(?P<model>[a-z]+)/$', 'ajax.views.generic_handler'),
                       )
