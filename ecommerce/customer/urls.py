from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='customer_home'),
    path('orders/', PurchasedProductsListView.as_view(), name='customer_orders'),
]