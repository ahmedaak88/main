from __future__ import unicode_literals
from django.contrib import admin
from django.contrib import admin
from .models import Coffe ,Roast ,Syrups ,Powders , Bean

class CoffeModelAdmin(admin.ModelAdmin):
	class Meta:
		model = Coffe

admin.site.register(Coffe, CoffeModelAdmin)
class RoastModelAdmin(admin.ModelAdmin):

	class Meta:
		model = Roast

admin.site.register(Roast, RoastModelAdmin)
class SyrupsModelAdmin(admin.ModelAdmin):

	class Meta:
		model = Syrups

admin.site.register(Syrups, SyrupsModelAdmin)
class PowdersModelAdmin(admin.ModelAdmin):

	class Meta:
		model = Powders

admin.site.register(Powders, PowdersModelAdmin)
class BeanModelAdmin(admin.ModelAdmin):

	class Meta:
		model = Bean

admin.site.register(Bean, BeanModelAdmin)