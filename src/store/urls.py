from django.urls import path
from .views import *

urlpatterns = [
	path('home/', home, name='home'),
	path('cart/', cart, name='cart'),
	path('checkout/', checkout, name='checkout'),
	path('update_item/', updateItem, name='update_item'),
]
