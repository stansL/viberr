from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from music.models import Album, Song
from music.serializers import AlbumSerializer, SongSerializer


# Use ViewSets with relations on Key fields to construct API endpoints
class AlbumViewSet(viewsets.ModelViewSet):
    """     API End Point that offers functionality for HTTP Methods on the Album Model
                Subject to user authentication    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    """     API End Point that offers functionality for HTTP Methods on the Song Model
                Subject to user authentication    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer


# Use Generic Views - makes work easier in django
class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    template_name = 'music/details.html'
    model = Album


class AlbumCreate(CreateView):
    model = Album
    fields = ['album_title', 'artist', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['album_title', 'artist', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
