import user

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from general.forms import ArtWorkForm
from general.models import ArtUser, ArtWork
from music.models import MTrack
from audiofield.forms import AudioFormField

class MTrackForm(ArtWorkForm):
    title = forms.CharField()
    content = AudioFormField()
    image = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = ArtWork
        fields = ('title', )

    def save(self, commit=True):
        artwork = super(ArtWorkForm, self).save(commit=False)
        artwork.title = self.cleaned_data["title"]

        if commit:
            artwork.save()
            mtrack = MTrack()
            mtrack.artwork = artwork
            mtrack.content = self.cleaned_data["content"]
            mtrack.image = self.cleaned_data["image"]
            mtrack.description = self.cleaned_data["description"]
            mtrack.save()
        return artwork
