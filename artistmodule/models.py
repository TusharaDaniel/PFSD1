from django.db import models

# Create your models here.
class ArtistDetails(models.Model):
    song_name = models.CharField(max_length=100,default='Default Song Name')
    artist_name = models.CharField(max_length=100, default='Unknown Artist')
    lyrics_by=models.CharField(max_length=255)
    album=models.CharField(max_length=255)
    GENRE_TYPE=[
        ('Popmusic','Pop music'),
        ('Indianpop','Indian-pop'),
        ('Jazz','jazz'),
        ('Bollywood','bollywood'),
        ('EDM','edm'),
        ('hollywood','Hollywood'),

    ]
    genre_type=models.CharField(max_length=20,choices=GENRE_TYPE)

def __str__(self):
    return self.artist_name
