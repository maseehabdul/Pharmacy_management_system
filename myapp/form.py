from django.forms import ModelForm
from .models import medicine,customer,dealer,purchase
from django import forms
from django.forms import *

class addmedicine(ModelForm):
    class Meta:
        model = medicine
        fields = '__all__'
        widgets = {
              'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
        }),
                'company': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'company'
        }),

           'cost': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'cost'
        }),
                'type': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'type'
        }),
        }
class addcustomer(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
        widgets = {
              'cus_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
        }),
                'address': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'address'
        }),

           'phone_no': TextInput (attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'number'
        }),
                'email': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'email'
        }),
        }

class adddealer(ModelForm):
    class Meta:
        model = dealer
        fields = '__all__'

        widgets = {
              'med_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'medicine name'
        }),
                'dealer_nam': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'dealer name'
        }),

           'cost': TextInput (attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'cost'
        }),
                'stock': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'stock'
        }),
                  'Description': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'description'
        }),
        }
class addpurchase(ModelForm):
    class Meta:
        model = purchase
        fields = '__all__'

        widgets = {
                'product_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'product name'
        }),
                'cus_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'customer name'
        }),

                'phone_no': TextInput (attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'number'
        }),
                'price': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'price'
        }),
                  'quantity': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'Quantity    '
        }),
        }
     
     
