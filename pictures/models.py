from __future__ import unicode_literals

from django.db import models

# Create your models here.
from general.models import ArtWork


class Picture(models.Model):
    artwork = models.OneToOneField(ArtWork, on_delete=models.CASCADE, related_name='picture')
    content = models.ImageField(blank=False, upload_to='get_picture_image_path')
    description = models.CharField(blank=True, max_length=255)
