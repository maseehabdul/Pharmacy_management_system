from django.forms import ModelForm
from .models import medicine
from django import forms
from django.forms import *

class addmedicine(ModelForm):
    class Meta:
        model = medicine
        fields = '__all__'
      
        widgets={
            'name':TextInput(attrs={
                'class':'form-control',
                'placeholder':'name',
                'style':'width:300px;padding:5px;'
            }),
               'company':TextInput(attrs={
                'class':'form-control',
                'placeholder':'company',
                'style':'width:300px;padding:5px;'
            }),
                'cost':TextInput(attrs={
                'class':'form-control',
                'placeholder':'cost',
                'style':'width:300px;padding:5px;'
            }),
           
        
               'type':TextInput(attrs={
                'class':'form-control',
                'placeholder':'type',
                'style':'width:300px;padding:5px;'
            }),
        }