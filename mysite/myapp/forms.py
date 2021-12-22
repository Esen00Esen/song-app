from django import forms
from .models import Song
from django.forms import ModelForm, fields

class SongForm(ModelForm):

    class Meta:
        model = Song
        fields = '__all__'

