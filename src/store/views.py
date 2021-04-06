from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
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

def updateItem(request):
	data		= json.loads(request.body)
	productId	= data['productId']
	action		= data['action']
	print(f'productId: {productId}\naction: {action}')

	account				= request.user.account
	product				= Product.objects.get(id=productId)
	order, created		= Order.objects.get_or_create(account=account)
	orderItem, created	= OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity += 1
	elif action == 'remove':
		orderItem.quantity -= 1
	
	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()
	
	return JsonResponse('Item added', safe=False)
