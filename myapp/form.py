from django import forms
from .models import medicine

class createmedicine(forms.ModelForm):
    class Meta:
        model = medicine
        fields = '_all_'