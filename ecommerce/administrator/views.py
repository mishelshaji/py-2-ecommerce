from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from product.models import Brand
from product.forms import BrandForm

# Create your views here.
@login_required
@user_passes_test(lambda x:x.is_admin)
def home(request):
    return render(request, 'administrator/home.html')

class BrandCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Brand
    template_name = "administrator/brand/create.html"
    success_url = '/administrator'
    form_class = BrandForm

    def test_func(self):
        return self.request.user.is_admin

class BrandListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Brand
    template_name = "administrator/brand/list.html"

    def test_func(self):
        return self.request.user.is_admin
