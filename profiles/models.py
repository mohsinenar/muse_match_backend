from django.contrib.auth.models import User
from django.db import models
from social_django.utils import load_strategy
import uuid
import os

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('profile_pictures', filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    looking_for = models.CharField(max_length=6, choices=GENDER_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField(default=18)

    # location = models.CharField(max_length=255, null=True, blank=True)
    # ethnicity = models.CharField(max_length=255, null=True, blank=True)
    # religion = models.CharField(max_length=255, null=True, blank=True)
    # education_level = models.CharField(max_length=255, null=True, blank=True)
    # occupation = models.CharField(max_length=255, null=True, blank=True)
    # height = models.PositiveIntegerField(null=True, blank=True)
    # body_type = models.CharField(max_length=255, null=True, blank=True)
    # interests = models.TextField(null=True, blank=True)
    # relationship_status = models.CharField(max_length=255, null=True, blank=True)
    # sexual_orientation = models.CharField(max_length=255, null=True, blank=True)
    # languages_spoken = models.CharField(max_length=255, null=True, blank=True)
    # smoking_habits = models.CharField(max_length=255, null=True, blank=True)
    # drinking_habits = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def spotify_token(self) -> str:
        social = self.user.social_auth.all().get(provider="spotify")
        strategy = load_strategy()
        social.refresh_token(strategy)
        return social.extra_data['access_token']


class ImageModel(models.Model):
    image = models.ImageField(upload_to=get_file_path, null=True)
    profile = models.ForeignKey(UserProfile, related_name="images", on_delete=models.CASCADE)


class ProfileView(models.Model):
    viewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='views')
    viewed_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='viewed')
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='likes_given')
    liked_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='likes_received')
    created_at = models.DateTimeField(auto_now_add=True)


class Pass(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='passes_given')
    passed_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='passes_received')
    created_at = models.DateTimeField(auto_now_add=True)


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
