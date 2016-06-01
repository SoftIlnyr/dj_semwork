from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from general.models import ArtUser


class ArtUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(ArtUserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
            artuser = ArtUser()
            artuser.user = user
            artuser.avatar = self.cleaned_data["avatar"]
            artuser.save()
        return user

class ArtUserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)
    username = forms.CharField(required=True)
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ()

    def update(self, user):
        # if len(self.cleaned_data["email"]) > 0:
        #     user.email = self.cleaned_data["email"]
        # if len(self.cleaned_data["username"]) > 0:
        #     user.username = self.cleaned_data["username"]
        # if len(self.cleaned_data["first_name"]) > 0:
        #     user.first_name = self.cleaned_data["first_name"]
        # if len(self.cleaned_data["last_name"]) > 0:
        #     user.last_name = self.cleaned_data["last_name"]
        # if len(self.cleaned_data.get('password1')) > 0:
        #     password1 = self.cleaned_data.get('password1')
        #     password2 = self.cleaned_data.get('password2')
        #     if password1 and password1 == password2:
        #         user.set_password(password1)
        #     else:
        #         raise forms.ValidationError("Passwords don't match")
        # if "username" in self.changed_data:
        #     user.username = self.cleaned_data.get("username")
        if "first_name" in self.changed_data:
            user.first_name = self.cleaned_data.get("first_name")
        if "last_name" in self.changed_data:
            user.last_name = self.cleaned_data.get("last_name")
        if "email" in self.changed_data:
            user.email = self.cleaned_data.get("email")
        if "password1" in self.changed_data:
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')
            if password1 and password1 == password2:
                user.set_password(password1)
            else:
                raise forms.ValidationError("Passwords don't match")
        user.save()
        artuser = user.artuser
        if "avatar" in self.changed_data:
            artuser.avatar = self.cleaned_data["avatar"]
        artuser.save()
        return user


class ArtWorkForm(forms.ModelForm):
    title = forms.CharField()
