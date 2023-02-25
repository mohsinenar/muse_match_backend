from django.contrib import admin

from profiles import models


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
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


@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    pass
