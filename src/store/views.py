from django.shortcuts import render

# Create your views here.

def home_view(request):
	context = {}
	return render(request, 'store/home.html', context)

def cart_view(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout_view(request):
	context = {}
	return render(request, 'store/checkout.html', context)
