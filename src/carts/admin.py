from django.contrib import admin

from .models import CartItem, Cart

class CartItemInline(admin.TabularInline):
	model = CartItem
	fields=('cart', 'items', 'quantity')

class CartAdmin(admin.ModelAdmin):
	inlines = [
		CartItemInline,
	]
	class Meta:
		model = Cart

admin.site.register(Cart, CartAdmin)