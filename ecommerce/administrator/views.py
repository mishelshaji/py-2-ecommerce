from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import CreateView
from product.models import Brand
from product.forms import BrandForm

# Create your views here.
@login_required
@user_passes_test(lambda x:x.is_admin)
def home(request):
    return render(request, 'administrator/home.html')

class BrandCreateView(CreateView):
    model = Brand
    template_name = "administrator/brand/create.html"
    success_url = '/administrator'
    form_class = BrandForm
