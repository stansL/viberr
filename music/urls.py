from django.conf.urls import url
from . import views

app_name = 'music'  # Bring in a namespace for the url names

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # music/album/create
    url(r'^album/create/$', views.AlbumCreate.as_view(), name='create'),

    # music/album/2/update
    url(r'^album/(?P<pk>[0-9]+)/update/$', views.AlbumUpdate.as_view(), name='update'),

    # music/album/2/update
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/album/2/
    url(r'^album/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
