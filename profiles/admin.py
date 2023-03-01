from django.contrib import admin

from profiles import models


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Pass)
class PassAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Match)
class MatchAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MusicGenre)
class MusicGenreAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MusicPreferencesProfile)
class MusicPreferencesProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Track)
class SongAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    pass
