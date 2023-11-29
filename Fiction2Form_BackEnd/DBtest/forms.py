from django import forms
from .models import Image, animal, car, character, geo, arch


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'photo']


class animalUploadForm(forms.ModelForm):
    class Meta:
        model = animal
        fields = ['title', 'photo']


class carUploadForm(forms.ModelForm):
    class Meta:
        model = car
        fields = ['title', 'photo']


class charUploadForm(forms.ModelForm):
    class Meta:
        model = character
        fields = ['title', 'photo']


class geoUploadForm(forms.ModelForm):
    class Meta:
        model = geo
        fields = ['title', 'photo']


class archUploadForm(forms.ModelForm):
    class Meta:
        model = arch
        fields = ['title', 'photo']

