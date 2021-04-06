from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

LABEL_CHOICES = (
    ('n', 'None'),
    ('primary', 'Bestseller'),
    ('danger', 'New'),
)

# def upload_location(instance, filename):
# 	file_path = f'prod/{instance.name}-{filename}'
# 	return file_path

class Product(models.Model):
	name			= models.CharField(max_length=50, null=False, blank=False, unique=True)
	price			= models.FloatField()
	label			= models.CharField(choices=LABEL_CHOICES, max_length=7, default=None)
	# image			= models.ImageField(upload_to=upload_location, null=True)

	def __str__(self):
		return self.name
	
	def get_status(self):
		if self.label == 'primary':
			return 'bestseller'
		else:
			return 'new'

class Order(models.Model):
	account			= models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
	date_ordered	= models.DateTimeField(auto_now_add=True)
	complete		= models.BooleanField(default=False)
	transaction_id	= models.CharField(max_length=100)
	
	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product			= models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order			= models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity		= models.IntegerField(default=0)
	date_added		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id)

class Shipping(models.Model):
	account			= models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
	order			= models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address			= models.CharField(max_length=200, null=False, blank=False)
	city			= models.CharField(max_length=25, null=False, blank=False)
	state			= models.CharField(max_length=25, null=False, blank=False)
	zipcode			= models.CharField(max_length=10, null=False, blank=False)
	date_added		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.zipcode
