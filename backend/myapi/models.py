from django.db import models

# Create your models here.
class Album(models.Model):
    albumName = models.CharField(max_length=60)
    imageUrl = models.CharField(max_length=500)
    artist = models.CharField(max_length=60)
    def __str__(self):
        return self.albumName

class Song(models.Model):
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    class Meta:
        unique_together = ['album', 'id']

    def __str__(self):
        return self.title