from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ArtUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artuser')
    followers = models.ManyToManyField('ArtUser', blank=True, related_name='following')
    favorites = models.ManyToManyField('ArtWork', blank=True, related_name='favorite')
    avatar = models.ImageField(u'avatar', upload_to='accounts/avatar/', blank=True, default='accouns/avatar/default.jpg')

    def __unicode__(self):
        return "%s" % (self.user.username)

class ArtWork(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(ArtUser)
    pub_date = models.DateTimeField()
    rating = models.IntegerField(default=0)
    type = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return "%s : %s (%s)" % (self.title, self.author.user.username, self.type )


class Comment(models.Model):
    artwork = models.ForeignKey(ArtWork)
    publisher = models.ForeignKey(ArtUser)
    text = models.TextField(blank=False, max_length=255)
    pub_date = models.DateTimeField()
    rating = models.IntegerField(default=0)