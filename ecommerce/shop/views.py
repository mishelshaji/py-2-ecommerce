from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from .models import *
from product.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
import stripe
import json

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        cart_items = Cart.objects.filter(user=self.request.user).select_related('product')
        for i in cart_items:
            total += i.product.price
        context['total'] = total
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

@csrf_exempt
# @require_POST
def create_checkout_token(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'inr',
                    'unit_amount': 2000,
                    'product_data': {
                        'name': 'Stubborn Attachments',
                        'images': ['https://i.imgur.com/EHyR2nP.png'],
                    },
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='https://testsite.com/success.html',
        cancel_url='https://testsite.com/cancel.html',
    )

    return JsonResponse(checkout_session)