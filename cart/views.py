from django.shortcuts import render
from .models import  *
from main.models import Coffe


def mycart(request):
	cart ,created = Cart.objects.get_or_create(user=request.user)
	item_id = request.GET.get("item")
	qty = request.GET.get("qty" , 1)

	if item_id:
		coffe = Coffe.objects.get(id=item_id)
		cart_item,created = CartItem.objects.get_or_create(cart=cart,items=coffe)
		try:
			if int(qty) < 1:
				cart_item.delete()
		except:
			raise Http404
		cart_item.quantity = int(qty)
		cart_item.save()



	return render(request, 'cart.html',{'cart': cart})
