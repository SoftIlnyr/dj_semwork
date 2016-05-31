from __future__ import unicode_literals

from django.db import models

# Create your models here.
from general.models import ArtWork


class Writing(models.Model):
    artwork = models.OneToOneField(ArtWork, on_delete=models.CASCADE, related_name='literature')
    content = models.TextField()
    description = models.CharField(blank=True, max_length=255)
