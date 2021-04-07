from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
# Create your views here.

def home(request):
	# consider removing below block
	if request.user.is_authenticated:
		account			= request.user.account
		order, created	= Order.objects.get_or_create(account=account, complete=False)
	else:
		items	= 0
		order	= {'get_cart_quantity': 0, 'get_cart_total': 0}
	#
	products	= Product.objects.all()
	context		= {'products': products, 'order': order}
	return render(request, 'store/home.html', context)

def cart(request):
	if request.user.is_authenticated:
		account			= request.user.account
		order, created	= Order.objects.get_or_create(account=account, complete=False)
		items			= order.orderitem_set.all()
	else:
		items	= []
		order	= {'get_cart_quantity': 0, 'get_cart_total': 0}
	context	= {'items': items, 'order': order}
	return render(request, 'store/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		account			= request.user.account
		order, created	= Order.objects.get_or_create(account=account, complete=False)
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

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		account = request.user.account
		order, created = Order.objects.get_or_create(account=account, complete=False)
		total = order.get_cart_total
		order.transaction_id = transaction_id
		order.complete = True
		order.save()

		Shipping.objects.create(
			account=account,
			order=order,
			address=data['shipping']['address'],
			city=data['shipping']['city'],
			state=data['shipping']['state'],
			zipcode=data['shipping']['zipcode'],
		)
	else:
		print('User is not logged in')
	return JsonResponse('Payment done', safe=False)
