from django.db import models


# Create your models here.
class medicines(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    med_company = models.CharField(max_length=20)
    med_cost = models.IntegerField()
    med_stock =models.IntegerField()










    
