from django import forms
from .models import ThreeDModel

class ThreeDModelForm(forms.ModelForm):
    class Meta:
        model = ThreeDModel
        fields = ['name', 'description', 'main_model_file', 'texture_file']
