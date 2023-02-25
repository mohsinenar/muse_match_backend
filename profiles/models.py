from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    looking_for = models.CharField(max_length=6, choices=GENDER_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.user.username


class MusicGenre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='music_genre_images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    genres = models.ManyToManyField('MusicGenre')
    followers = models.ManyToManyField(UserProfile, related_name='following_artists')

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    genres = models.ManyToManyField('MusicGenre')

    def __str__(self):
        return self.title


class MusicPreferencesProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='music_preferences')
    genres = models.ManyToManyField('MusicGenre', blank=True)
    artists = models.ManyToManyField(Artist)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return f"{self.user}'s music preferences"
