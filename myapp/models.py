from django import forms
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =20)
    company = models.CharField(max_length =20)
    cost = models.IntegerField()
    type = models.CharField(max_length =20)

class customer(models.Model):
     id = models.AutoField(primary_key=True)
     cus_name = models.CharField(max_length =20)
     address = models.CharField(max_length =20)
     phone_no = PhoneNumberField(null=False, blank=False, unique=True)
     email = models.EmailField(max_length =254)

class purchase(models.Model):
      id = models.AutoField(primary_key=True)
      product_name = models.CharField(max_length =20,null=True)
    #   cus_name = models.CharField(max_length =20,blank=False)
    #   phone_no = PhoneNumberField(null=False, blank=True, unique=True,blank=False)
      price = models.IntegerField()
      quantity = models.IntegerField()  

class dealer(models.Model):
    id = models.AutoField(primary_key=True)
    med_name = models.CharField(max_length =20)
    dealer_nam = models.CharField(max_length =20)
    cost = models.IntegerField()
    stock = models.IntegerField()
    Description = models.CharField(max_length=100)













    
