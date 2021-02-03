from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', CartListView.as_view(), name='shop_cart_home'),
    path('cart/add/<id>/', add_to_cart, name='shop_add_cart'),

    path('create-checkout-session/', create_checkout_token, name='create_checkout_token')
]
