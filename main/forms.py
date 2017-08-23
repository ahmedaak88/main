from django import forms
from django.contrib.auth.models import User 
from .models import *


class UserSignUp(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']
		widgets= {
			'password': forms.PasswordInput(),
		}
class UserLogin(forms.Form):
	username= forms.CharField(required=True)
	password= forms.CharField(required=True,widget=forms.PasswordInput())
class CoffeForm(forms.ModelForm):
	class Meta:
		model = Coffe
		fields = ['name','espresso','bean', 'syrups','roast','powders','water','steamed_milk','foam','extra_instructions']




class AdressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = ['city' ,'block','street' , 'building', 'floor','apt_number','extra_direction']

class CityForm(forms.ModelForm):
	class Meta:
		model = City 
		fields = ['name']




class RoastForm(forms.ModelForm):
	class Meta:
		model = Roast
		fields = ['name','price']
		widgets={
		'name': forms.TextInput(attrs={'id': 'roast_name', 'required': True, 'placeholder': 'Say something...'}),
		'price': forms.NumberInput(attrs={'id': 'roast_price'}),
		'publish': forms.DateInput(attrs={"type":"date"}),
		}
class SyrupsForm(forms.ModelForm):
	class Meta:
		model = Syrups
		fields = ['name','price']
		widgets={
		'publish':forms.DateInput(attrs={"type":"date"}),
		}
class PowdersForm(forms.ModelForm):
	class Meta:
		model = Powders
		fields = ['name','price']
		widgets={
		'publish':forms.DateInput(attrs={"type":"date"}),
		}
class BeanForm(forms.ModelForm):
	class Meta:
		model = Bean
		fields = ['name','price']
		widgets={
		'publish':forms.DateInput(attrs={"type":"date"}),
		}