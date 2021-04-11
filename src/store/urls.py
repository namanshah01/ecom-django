from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home'),
	path('cart/', cart, name='cart'),
	path('checkout/', checkout, name='checkout'),
	path('update_item/', updateItem, name='update_item'),
	path('process_order/', processOrder, name='process_order'),
	path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
	path('product/create/', ProductCreateView.as_view(), name='product_create'),
	path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
	path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
