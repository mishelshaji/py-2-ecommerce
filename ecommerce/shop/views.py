from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from .models import *
from product.models import Product

# Create your views here.
@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    if Cart.objects.filter(user=request.user, product=product).exists():
        return redirect("shop_cart_home") # redirect to cart view page
    else:
        Cart.objects.create(user=request.user, product=product)
        return redirect("shop_cart_home") # redirect to cart view page

class CartListView(ListView):
    template_name = "shop/cart.html"
    model = Cart
    
    def get_queryset(self):
        queryset = super(CartListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user).select_related('product')
        return queryset
