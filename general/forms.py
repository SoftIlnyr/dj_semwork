from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from general.models import ArtUser


class ArtUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    # avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def save(self, commit=True):
        user = super(ArtUserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
            artuser = ArtUser()
            artuser.user = user
            artuser.save()
        return user