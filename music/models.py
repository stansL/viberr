from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
class Album(models.Model):
    album_title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100)
    file_type = models.CharField(max_length=5)

    def __str__(self):
        return self.song_title
