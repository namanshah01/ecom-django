from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
	products	= Product.objects.all()
	context		= {'products': products}
	return render(request, 'store/home.html', context)

def cart(request):
	if request.user.is_authenticated:
		account			= request.user.account
		order, created	= Order.objects.get_or_create(account=account)
		items			= order.orderitem_set.all()
	else:
		items	= []
		order	= {'get_cart_quantity': 0, 'get_cart_total': 0}
	context	= {'items': items, 'order': order}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		account			= request.user.account
		order, created	= Order.objects.get_or_create(account=account)
		items			= order.orderitem_set.all()
	else:
		items	= []
		order	= {'get_cart_quantity': 0, 'get_cart_total': 0}
	context	= {'items': items, 'order': order}
	return render(request, 'store/checkout.html', context)
