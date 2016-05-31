# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-31 12:58
from __future__ import unicode_literals

import audiofield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '0002_auto_20160531_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='MTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', audiofield.fields.AudioField(blank=True, help_text='Allowed type - .mp3, .wav, .ogg', upload_to='music_tracks/')),
                ('image', models.ImageField(upload_to='get_music_image_path')),
                ('description', models.CharField(max_length=255)),
                ('artwork', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mtrack', to='general.ArtWork')),
            ],
        ),
    ]
