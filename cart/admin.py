from django.contrib import admin
from .models import *

# Register your models here.
class CartAdmin(admin.ModelAdmin):
	class Meta:
		model = Cart

admin.site.register(Cart, CartAdmin)



class CartItemAdmin(admin.ModelAdmin):
	class Meta:
		model = CartItem

admin.site.register(CartItem, CartItemAdmin)