from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='admin_home'),
    path('brand/create/', BrandCreateView.as_view(), name='admin_brand_create'),
]