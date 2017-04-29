from django.contrib import admin
from .models import UserCheckOut, UserAddress, Order

admin.site.register(UserCheckOut)
admin.site.register(UserAddress)
admin.site.register(Order)
