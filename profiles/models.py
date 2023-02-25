import dataclasses
from typing import Type

from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


@dataclasses.dataclass
class SpotifyAuthData:
    auth_time: int
    refresh_token: str
    access_token: str
    token_type: str

    @classmethod
    def from_dict(cls, data_dict):
        auth_time = data_dict.get("auth_time")
        refresh_token = data_dict.get("refresh_token")
        access_token = data_dict.get("access_token")
        token_type = data_dict.get("token_type")
        return cls(auth_time=auth_time, refresh_token=refresh_token,access_token=access_token,token_type=token_type)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    looking_for = models.CharField(max_length=6, choices=GENDER_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.user.username

    def spotify(self) -> Type[SpotifyAuthData]:
        spotify_auth_data = self.user.social_auth.all().get(provider="spotify").extra_data
        return SpotifyAuthData.from_dict(spotify_auth_data)


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
