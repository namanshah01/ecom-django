from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# from .settings import AUTH_USER_MODEL
from ecomweb.settings import AUTH_USER_MODEL

# Create your models here.

LABEL_CHOICES = (
    ('n', 'None'),
    ('primary', 'Bestseller'),
    ('danger', 'New'),
)

def upload_location(instance, filename):
	file_path = f'prod/{instance.name}-{filename}'
	return file_path

class Product(models.Model):
	name			= models.CharField(max_length=50, null=False, blank=False, unique=True)
	price			= models.FloatField()
	label			= models.CharField(choices=LABEL_CHOICES, max_length=7, default=None)
	image			= models.ImageField(upload_to=upload_location, null=True)

	def __str__(self):
		return self.name
	
	def get_status(self):
		if self.label == 'primary':
			return 'bestseller'
		else:
			return 'new'
	
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.image.path)
		if img.width>525 or img.height>300:
			output_size = (525, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

class Order(models.Model):
	account			= models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
	date_ordered	= models.DateTimeField(auto_now_add=True)
	complete		= models.BooleanField(default=False)
	transaction_id	= models.CharField(max_length=100)
	
	def __str__(self):
		return str(self.id)
	
	@property
	def get_cart_total(self):
		orderitems	= self.orderitem_set.all()
		total		= sum([orderitem.get_total for orderitem in orderitems])
		return total
	
	@property
	def get_cart_quantity(self):
		orderitems	= self.orderitem_set.all()
		total		= sum([orderitem.quantity for orderitem in orderitems])
		return total

class OrderItem(models.Model):
	product			= models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order			= models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity		= models.IntegerField(default=0)
	date_added		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.id)
	
	@property
	def get_total(self):
		return self.product.price*self.quantity

class Shipping(models.Model):
	account			= models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
	order			= models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address			= models.CharField(max_length=200, null=False, blank=False)
	city			= models.CharField(max_length=25, null=False, blank=False)
	state			= models.CharField(max_length=25, null=False, blank=False)
	zipcode			= models.CharField(max_length=10, null=False, blank=False)
	date_added		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.zipcode
