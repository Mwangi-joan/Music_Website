from django import forms
from .models import Album,Song
from django.contrib.auth.models import User

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['name', 'artist', 'year', 'cover', 'genre']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'audio']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']





