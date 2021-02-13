from django.shortcuts import render
from product.models import Product


# Create your views here.
def home(request):
    context = {}
    context['product_list'] = Product.objects.all()[:15]
    return render(request, 'user/home.html', context)
