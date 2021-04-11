from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import *
from django.http import JsonResponse
import json
import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
# Create your views here.

@login_required(login_url='/login/')
def home(request):
	# cart number
	account			= request.user
	order, created	= Order.objects.get_or_create(account=account, complete=False)

	# search
	query = ''
	# if request.GET:
	# 	query = request.GET['q']
	# 	products = get_queryset(query)
	# else:
	# 	products	= Product.objects.all().order_by('id')

	# pagination
	products	= Product.objects.all().order_by('id')
	object_list = products
	paginator = Paginator(object_list, 6)
	page = request.GET.get('page')
	try:
		prod_list = paginator.page(page)
	except PageNotAnInteger:
		prod_list = paginator.page(1)
	except EmptyPage:
		prod_list = paginator.page(paginator.num_pages)
	
	context = {'products': products, 'order': order, 'page': page, 'prod_list': prod_list, 'page_obj': paginator, 'query': query}
	return render(request, 'store/home.html', context)

@login_required(login_url='/login/')
def cart(request):
	account			= request.user
	order, created	= Order.objects.get_or_create(account=account, complete=False)
	items			= order.orderitem_set.all()
	context	= {'items': items, 'order': order}
	return render(request, 'store/cart.html', context)

@login_required(login_url='/login/')
def checkout(request):
	account			= request.user
	order, created	= Order.objects.get_or_create(account=account, complete=False)
	items			= order.orderitem_set.all()
	context	= {'items': items, 'order': order}
	return render(request, 'store/checkout.html', context)

@login_required(login_url='/login/')
def updateItem(request):
	data		= json.loads(request.body)
	productId	= data['productId']
	action		= data['action']
	print(f'productId: {productId}\naction: {action}')

	account				= request.user
	product				= Product.objects.get(id=productId)
	order, created		= Order.objects.get_or_create(account=account, complete=False)
	orderItem, created	= OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity += 1
	elif action == 'remove':
		orderItem.quantity -= 1
	
	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()
	
	return JsonResponse('Item added', safe=False)

@login_required(login_url='/login/')
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		account = request.user
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

def get_queryset(query=None):
	queryset = []
	if (query=='' or query==None):
		products = Product.objects.all()
	else:
		queries = query.split(" ")
		for q in queries:
			products = Product.objects.filter(Q(name__icontains=q)).distinct()
			# posts = Product.objects.filter(Q(name__icontains=q) | Q(label__icontains=q)).distinct()
	return products

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_admin


class ProductDetailView(DetailView):
	model = Product
	template_name = 'store/product_detail.html'
	context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
	model = Product
	fields = '__all__'
	template_name = 'store/product_create.html'

	def get_success_url(self):
		return reverse('product_detail', kwargs={'pk': self.object.pk})

class ProductUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
	model = Product
	fields = '__all__'
	template_name = 'store/product_update.html'

	def get_success_url(self):
		return reverse('product_detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
	model = Product
	success_url = '/'
	template_name = 'store/product_delete.html'
