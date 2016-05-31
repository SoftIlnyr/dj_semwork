from __future__ import unicode_literals

import os

from django.db import models
from audiofield.models import AudioField

# Create your models here.
from SoftArts2 import settings
from general.models import ArtWork


class MTrack(models.Model):
    artwork = models.OneToOneField(ArtWork, on_delete=models.CASCADE, related_name="mtrack")
    content = AudioField(upload_to='music_tracks/', blank=True,
                         ext_whitelist=(".mp3", ".wav", ".ogg"),
                         help_text=("Allowed type - .mp3, .wav, .ogg"))
    image = models.ImageField(upload_to=u'get_music_image_path', blank=True)
    description = models.CharField(blank=True, max_length=255)

    def audio_file_player(self):
        """audio player tag for admin"""
        if self.audio_file:
            file_url = settings.MEDIA_URL + str(self.content)
            player_string = '<ul class="playlist"><li style="width:250px;">\
        <a href="%s">%s</a></li></ul>' % (file_url, os.path.basename(self.audio_file.name))
            return player_string

    # Add this method to your model

    audio_file_player.allow_tags = True
    audio_file_player.short_description = ('Audio file player')
