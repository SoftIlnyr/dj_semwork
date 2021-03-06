# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-31 12:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artuser',
            name='avatar',
            field=models.ImageField(blank=True, default='accouns/avatar/default.jpg', upload_to='accounts/avatar/', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='artuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='artuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
