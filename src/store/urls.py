from django.urls import path
from .views import home_view, cart_view, checkout_view

urlpatterns = [
	path('home/', home_view, name='home'),
	path('cart/', cart_view, name='cart'),
	path('checkout/', checkout_view, name='checkout'),
]
