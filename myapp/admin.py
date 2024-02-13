from django.contrib import admin

# Register your models here.
from .models import medicine,dealer,customer,purchase

admin.site.register(medicine)
admin.site.register(customer)
admin.site.register(dealer)
admin.site.register(purchase)
