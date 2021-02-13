from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from shop.models import PurchasedProducts
from django.views.generic import ListView

# Create your views here.
@login_required
@user_passes_test(lambda x:x.is_customer)
def home(request):
    return render(request, 'customer/home.html')

class PurchasedProductsListView(ListView):
    model = PurchasedProducts
    template_name = "customer/order.html"
    context_object_name = 'data'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).prefetch_related('product')
