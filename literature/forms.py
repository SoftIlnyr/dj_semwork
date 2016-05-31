import user

from django.contrib.auth.forms import UserCreationForm
from django import forms

from general.forms import ArtWorkForm
from general.models import ArtUser, ArtWork

class WritingForm(ArtWorkForm):
    title = forms.CharField()
    content = forms.CharField(required=True, widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = ArtWork
        fields = ('title', )

