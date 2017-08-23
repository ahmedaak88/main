from django.db import models
from django.contrib.auth.models import User
from main.models import Coffe 
from django.db.models.signals import post_save, pre_save, post_delete
from decimal import Decimal


class CartItem(models.Model):
	cart = models.ForeignKey("Cart")
	items = models.ForeignKey(Coffe)
	quantity = models.PositiveIntegerField(default=1)
	line_item_total = models.DecimalField(max_digits= 6 , decimal_places=3)
	def __str__(self):
		return self.items.name

def cart_item_pre_save(sender, instance,*args,**kwargs):
	qty = instance.quantity
	if qty >= 1:
		price = instance.items.price
		total= price * qty
		instance.line_item_total = total 
pre_save.connect(cart_item_pre_save , sender=CartItem)

def cart_item_post_save(sender, instance,*args,**kwargs):
	instance.cart.update_subtotal()

post_save.connect(cart_item_post_save, sender=CartItem)
post_delete.connect(cart_item_post_save, sender=CartItem)

class Cart(models.Model):
	user = models.ForeignKey(User)
	items = models.ManyToManyField(Coffe, through=CartItem)
	subtotal = models.DecimalField(max_digits= 6 , decimal_places=3 , default=1.000)
	delivery_total = models.DecimalField(max_digits= 6 , decimal_places=3, default=1.000)
	total = models.DecimalField(max_digits=6,decimal_places=3,default=1.000)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	def __str__(self):
		return self.user.username


	def update_subtotal(self):
		x= Decimal(0) 
		items = self.cartitem_set.all()
		for item in items:
			x += item.line_item_total
		self.subtotal  = Decimal(x)
		self.save()

def delivery_and_total(sender, instance,*args,**kwargs):
	subtotal = instance.subtotal
	delivery_total = Decimal(2.000)
	total = Decimal(subtotal) + Decimal(delivery_total)
	instance.delivery_total = delivery_total
	instance.total = total

pre_save.connect(delivery_and_total, sender=Cart)