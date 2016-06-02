import os

from audiofield.admin import AudioFileAdmin
from django.contrib import admin

# Register your models here.
# add 'audio_file_player' tag to your admin view
from music.models import MTrack


class MTrackAdmin(admin.ModelAdmin):
    list_display = ["id","artwork", "content", "image", "description"]

    class Meta:
        model = MTrack


admin.site.register(MTrack, MTrackAdmin)
