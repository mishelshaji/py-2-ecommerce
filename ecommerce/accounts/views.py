from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import *

# Create your views here.
def user_login(request):
    context = {}
    context['reg_form'] = UserForm()
    context['details_form'] = CustomerDetailsForm()
    return render(request, 'accounts/login.html', context)

@require_POST
def register(request):

    uf = UserForm(request.POST)
    cdf = CustomerDetailsForm(request.POST)

    if uf.is_valid() and cdf.is_valid():
        user = uf.save(commit=False)
        password = uf.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        data = cdf.save(commit=False)
        data.user = user
        data.save()
        messages.success(request, "Please login now")
        return redirect('accounts_login')
    
    context = {}
    context['reg_form'] = uf
    context['details_form'] = cdf
    return render(request, 'accounts/login.html', context)
