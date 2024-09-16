from django.contrib import admin
from .models import CoffeeUser, Coffee

# Register your models here.
admin.site.register(CoffeeUser)
admin.site.register(Coffee)