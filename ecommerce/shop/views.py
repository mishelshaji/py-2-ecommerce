from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from .models import *
from product.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
from django.urls import reverse
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

    cart = Cart.objects.filter(user=request.user)

    item_data = []
    for c in cart:
        data = {
            'price_data': {
                    'currency': 'inr',
                    'product_data': {
                        'name': '',
                    },
                'unit_amount': 0,
            },
            'quantity': 1,
        }
        data['price_data']['currency'] = 'inr'
        data['price_data']['product_data']['name'] = c.product.name
        data['price_data']['unit_amount'] = int(c.product.price) * 100
        data['quantity'] = 1
        item_data.append(data)

    tid = uuid.uuid4()

    SUCCESS_URL = reverse('shop_confirm_payment', kwargs={'sid':tid})
    print(SUCCESS_URL)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=item_data,
        mode='payment',
        success_url = request.build_absolute_uri(SUCCESS_URL),
        cancel_url='https://testsite.com/cancel.html',
    )

    sess_id = checkout_session.id
    payment_intent = checkout_session.payment_intent

    for p in cart:
        Order.objects.create(
            session_id = sess_id,
            intent_id = payment_intent,
            product = p.product,
            transaction_id = tid
        )

    return JsonResponse(checkout_session)

def confirm_payment(request, sid):
    session_status = str

    try:
        orders = Order.objects.filter(transaction_id=sid).exists()
        if orders:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            sid = Order.objects.filter(transaction_id=sid).first().session_id
            payment_details = stripe.checkout.Session.retrieve(sid)

            if payment_details['payment_status'] == 'paid':
                Order.objects.filter(session_id=sid).update(is_success=True)

                # Clearing the shopping cart
                Cart.objects.filter(user=request.user).delete()

                confirmed_orders = Order.objects.filter(session_id=sid, is_success=True)
                if confirmed_orders:
                    for i in confirmed_orders:
                        product = i.product
                        PurchasedProducts.objects.create(user=request.user, product=product)
        return redirect('user_home')
    except Exception as e:
        print('👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍')
        print(e)
        return redirect('cart_home')

