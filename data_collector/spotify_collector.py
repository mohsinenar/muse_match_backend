import django

django.setup()

import tekore as tk
from profiles import models


class SpotifyCollector:
    def __init__(self, profile: models.UserProfile):
        self._profile = profile
        self.spotify = tk.Spotify(profile.spotify_token)

    def update_artists(self):
        artists = self.spotify.followed_artists()
        for artist in artists.items:
            artist_object, _ = models.Artist.objects.get_or_create(name=artist.name, defaults={"spotify_id": artist.id})
            artist_object.followers.add(self._profile)
            for genre in artist.genres:
                artist_object.genres.get_or_create(name=genre)

    def saved_tracks(self):
        tracks = self.spotify.saved_tracks()
        for track in tracks.items:
            track.track
            print(track.track)


profiles = models.UserProfile.objects.all()
for p in profiles:
    collector = SpotifyCollector(p)
    collector.saved_tracks()
