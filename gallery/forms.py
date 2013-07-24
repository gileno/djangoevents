#encoding: utf-8

from django import forms
from django.forms.models import inlineformset_factory

from .models import Album, Photo

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        exclude = ['event']

class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo

PhotoFormset = inlineformset_factory(Album, Photo, extra=1)