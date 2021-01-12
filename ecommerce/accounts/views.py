from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import *

# Create your views here.
def user_login(request):
    if request.method == "GET":
        context = {}
        context['login_form'] = AuthenticationForm()
        context['reg_form'] = UserForm()
        context['details_form'] = CustomerDetailsForm()
        return render(request, 'accounts/login.html', context)
    elif request.method == "POST":
        lf = AuthenticationForm(data=request.POST)
        if lf.is_valid():
            username = lf.cleaned_data.get('username')
            password = lf.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_customer:
                    return redirect('customer_home')
                elif user.is_admin:
                    return redirect('admin_home')
        context = {}
        context['login_form'] = lf
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
    context['login_form'] = AuthenticationForm()
    context['reg_form'] = uf
    context['details_form'] = cdf
    return render(request, 'accounts/login.html', context)
