from __future__ import unicode_literals
from django.contrib.auth import authenticate , login ,logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from .forms import  *
from django.contrib import messages
import json
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User 
from decimal import Decimal

def userlogin(request):
    context={}
    form = UserLogin()
    context['form'] = form 
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user= authenticate(username=username,password=password)
            if auth_user is not None:
                login(request,auth_user)
                return redirect("main:home")

            messages.warning(request,"wrong user name or password")
            return redirect("main:login")
        messages.warning(request,form.errors)
        return redirect("main:login")
    return render(request, 'login.html',context)


def usersignup(request):
    context={}
    form = UserSignUp()
    context['form'] = form 
    if request.method == "POST":
        form = UserSignUp(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            password = user.password
            user.set_password(password)
            user.save()
            auth_user= authenticate(username=username,password=password)
            login(request,auth_user)
            return redirect("main:home")
        messages.error(request,form.errors)
        return redirect("main:signup")
    return render(request, 'signup.html',context)

def userlogout(request):
    logout(request)
    return redirect("main:home")




def main_home(request):
	x = Coffe.objects.all()

	context = {
	    "user": request.user,
	    "details" : x,
	}
	return render(request, 'home.html', context)
def coffe_details(request,post_id):
	obj = get_object_or_404(Coffe , id=post_id)
	syr= ""
	powder = ""
	syr_price = 0
	powder_price = 0 
	for x in obj.syrups.all():
		syr += x.name + " ,"
		syr_price +=x.price
	for x in obj.powders.all():
		powder += x.name + " ,"
		powder_price += x.price
	

	context = {
	"powder":powder,
	"powder_price":powder_price,
	"syr_price":syr_price,
	"syr": syr,
	"user": request.user,
	"details":obj,
	}
	return render(request,'details.html',context)

def admin_view(request):
	users = User.objects.all()
	coffe = Coffe.objects.all()
	address = Address.objects.all()
	cont = {
	"users":users,
	"coffe":coffe,
	"address":address,
	}
	return render(request,'admin_view.html',cont)


def ingredents(request):
	x = Syrups.objects.all()
	y = Powders.objects.all()
	s = Bean.objects.all()
	r = Roast.objects.all()


	context = {
	    "user": request.user,
	    "syrups" : x,
	    "powders":y,
	    "beans":s,
	    "roasts":r,
	}
	return render(request, 'ingredents.html', context)



def bean_create(request):
	form = BeanForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj= form.save(commit=False)
		obj.author = request.user
		obj.save()
		messages.success(request,"you have created a new bean")
		return redirect("main:home")
	context = {
		"form": form,
		"user": request.user
	}
	return render(request, 'bean_create.html',context)


def syrups_create(request):
	form = SyrupsForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj= form.save(commit=False)
		obj.author = request.user
		obj.save()
		messages.success(request,"you have created a new syrup")
		return redirect("main:home")
	context = {
		"form": form,
		"user": request.user
	}
	return render(request, 'syrups_create.html',context)

def roast_create(request):
	form = RoastForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj= form.save(commit=False)
		obj.author = request.user
		obj.save()
		messages.success(request,"you have created a new bean")
		return redirect("main:home")
	context = {
		"form": form,
		"user": request.user
	}
	return render(request, 'roast_create.html',context)


def powders_create(request):
	form = PowdersForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj= form.save(commit=False)
		obj.author = request.user
		obj.save()
		messages.success(request,"you have created a new bean")
		return redirect("main:home")
	context = {
		"form": form,
		"user": request.user
	}
	return render(request, 'powder_create.html',context)


def address_create(request):
	form = AdressForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.author = request.user 
		obj.save()
		messages.success(request,"your address has been submited")
		return redirect("main:home")
	context = {
	"form":form,
	"user":request.user
	}
	return render(request,'address_create.html',context)
def city_create(request):
	form = CityForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False) 
		obj.save()
		messages.success(request,"a City has been added")
		return redirect("main:home")
	context = {
	"form":form,
	"user":request.user
	}
	return render(request,'city_create.html',context)

def coffe_create(request):
	form = CoffeForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		obj = form.save(commit=False)
		syrups_price = 0
		powders_price = 0
		obj.price = 0
		obj.save()
		form.save_m2m()
		y = obj.syrups.all()
		for x in y:
			syrups_price+= x.price
		for s in obj.powders.all():
			powders_price += s.price

		obj.price = 3 + obj.bean.price +  obj.roast.price +  int(obj.foam * 1) + int(obj.espresso * 1) + syrups_price + powders_price
		if obj.water:
			obj.price = obj.price + 1
		if obj.steamed_milk:
			obj.price = obj.price + 1
		obj.author = request.user 
		obj.save()
		

		messages.success(request,"your coffe is created")
		return redirect ("main:home")

	context = {
		"form": form,
		"user": request.user
	}
	return render(request, 'coffe_create.html',context)

def create_widget(request):
	total = Decimal(0)
	bean_id = request.GET.get('bean')
	if bean_id :
		total+= Bean.objects.get(id=bean_id).price

	roast_id = request.GET.get('roast')
	if roast_id:
		total += Roast.objects.get(id=roast_id).price

	shots = request.GET.get('espresso_shots')
	total+= int(shots) * Decimal(0.200)

	milk = request.GET.get("milk")
	if milk == 'true':
		total += Decimal(0.250)

	syrups = json.loads(request.GET.get('syrups'))
	for syrup in syrups:
		total += Syrups.objects.get(id=syrup).price

	powders = json.loads(request.GET.get('powders'))
	for powder in powders:
		total += Powders.objects.get(id=powder).price
	print (round(total,3))
	return JsonResponse(round(total,3) , safe=False)


def coffe_update(request, post_id):
	obj = get_object_or_404(Coffe , id=post_id)
	form = CoffeForm(request.POST or None ,request.FILES or None,instance=obj)
	if form.is_valid():

		obj.price = 0 
		form.save(commit=False)
		form.save_m2m()
		syrups_price = 0 
		powders_price = 0 
		y = obj.syrups.all()
		for x in y:
			syrups_price+= x.price
		for s in obj.powders.all():
			powders_price += s.price

		obj.price = 3 + obj.bean.price +  obj.roast.price +  int(obj.foam * 1) + int(obj.espresso * 1) + syrups_price + powders_price
		if obj.water:
			obj.price = obj.price + 1
		if obj.steamed_milk:
			obj.price = obj.price + 1
		form.save()


	

		messages.success(request,"your coffe has been updated")
		return redirect ("main:home")

	context = {
	"user":request.user,
	"form": form,
	"obj": obj,
	}
	return render(request, 'coffe_update.html',context)

def syrups_update(request, post_id):
	obj = get_object_or_404(Syrups , id=post_id)
	form = SyrupsForm(request.POST or None ,request.FILES or None,instance=obj)
	if form.is_valid():
		form.save()
		return redirect("main:ingredents")
	context = {
	"user":request.user,
	"form": form,
	"obj": obj,
	}
	return render(request, 'syrups_update.html',context)
def powders_update(request, post_id):
	obj = get_object_or_404(Syrups , id=post_id)
	form = PowdersForm(request.POST or None ,request.FILES or None,instance=obj)
	if form.is_valid():
		form.save()
		return redirect("main:ingredents")
	context = {
	"user":request.user,
	"form": form,
	"obj": obj,
	}
	return render(request, 'powders_update.html',context)
def bean_update(request, post_id):
	obj = get_object_or_404(Syrups , id=post_id)
	form = BeanForm(request.POST or None ,request.FILES or None,instance=obj)
	if form.is_valid():
		form.save()
		return redirect("main:ingredents")
	context = {
	"user":request.user,
	"form": form,
	"obj": obj,
	}
	return render(request, 'bean_update.html',context)
def roast_update(request, post_id):
	obj = get_object_or_404(Syrups , id=post_id)
	form = RoastForm(request.POST or None ,request.FILES or None,instance=obj)
	if form.is_valid():
		form.save()
		return redirect("main:ingredents")
	context = {
	"user":request.user,
	"form": form,
	"obj": obj,
	}
	return render(request, 'roast_update.html',context)

def coffe_delete(request, post_id):

    post_obj = Coffe.objects.get(id=post_id)
    post_obj.delete()
    messages.warning(request, "the coffe has been deleted")
    return redirect("main:home")
def syrups_delete(request, post_id):

    post_obj = Syrups.objects.get(id=post_id)
    post_obj.delete()
    messages.warning(request, "the object has been deleted")
    return redirect("main:ingredents")
def powders_delete(request, post_id):

    post_obj = Powders.objects.get(id=post_id)
    post_obj.delete()
    messages.warning(request, "the object has been deleted")
    return redirect("main:ingredents")
def bean_delete(request, post_id):

    post_obj = Bean.objects.get(id=post_id)
    post_obj.delete()
    messages.warning(request, "the object has been deleted")
    return redirect("main:ingredents")
def roast_delete(request, post_id):

    post_obj = Roast.objects.get(id=post_id)
    post_obj.delete()
    messages.warning(request, "the object has been deleted")
    return redirect("main:ingredents")


