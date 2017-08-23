from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User 



class Bean(models.Model):
	name = models.CharField(max_length=200)
	price =models.DecimalField(max_digits = 5 ,decimal_places=2)
	def __str__(self):
		return self.name
class Roast(models.Model):
	name = models.CharField(max_length=200)
	price =models.DecimalField(max_digits = 5, decimal_places=2)
	def __str__(self):
		return self.name
class Syrups(models.Model):
	name = models.CharField(max_length=200)
	price =models.DecimalField(max_digits = 5, decimal_places=2)
	def __str__(self):
		return self.name
class Powders(models.Model):
	name = models.CharField(max_length=200)
	price =models.DecimalField(max_digits = 5, decimal_places=2)
	def __str__(self):
		return self.name


class City(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Address(models.Model):
	author = models.ForeignKey(User)
	city = models.ForeignKey(City)
	block = models.CharField(max_length=200)
	street = models.CharField(max_length=200)
	building = models.CharField(max_length=200)
	floor = models.CharField(max_length=200)
	apt_number = models.IntegerField(default=0 , null=True)
	extra_direction = models.TextField(null=True)
	def __str__(self):
		return self.author

def get_first_model1():
    return [Powders.objects.first()
    ]
def get_first_model2():
    return [Syrups.objects.first()
    ]

class Coffe(models.Model):
	author = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=255)
	espresso = models.PositiveIntegerField(null=True, default=0)
	bean = models.ForeignKey(Bean,null=True)
	roast = models.ForeignKey(Roast, null=True)
	syrups = models.ManyToManyField(Syrups,blank=True, default=get_first_model1)
	powders= models.ManyToManyField(Powders,blank=True , default=get_first_model1)
	water =  models.FloatField(default=0,null=True)
	steamed_milk = models.BooleanField(default=False)
	foam = models.FloatField(null=True ,default=0)
	extra_instructions = models.TextField(null=True)
	price = models.DecimalField(max_digits = 5, decimal_places=2)
	# address = models.ForeignKey(Address)


	def __str__(self):
		return "%s with %s %s" %(
			self.name , " ,".join(x.name for x in self.syrups.all()) ," ,".join(s.name for s in self.powders.all()),)




