from django.contrib.auth.models import User
from django.db import models
from social_django.utils import load_strategy

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

    @property
    def spotify_token(self) -> str:
        social = self.user.social_auth.all().get(provider="spotify")
        strategy = load_strategy()
        social.refresh_token(strategy)
        return social.extra_data['access_token']


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
    spotify_id = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    genres = models.ManyToManyField('MusicGenre')
    followers = models.ManyToManyField(UserProfile, related_name='following_artists')

    def __str__(self):
        return self.name


class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    genres = models.ManyToManyField('MusicGenre')

    def __str__(self):
        return self.title


class MusicPreferencesProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='music_preferences')
    genres = models.ManyToManyField('MusicGenre', blank=True)
    artists = models.ManyToManyField(Artist)
    track = models.ManyToManyField(Track)

    def __str__(self):
        return f"{self.user}'s music preferences"
