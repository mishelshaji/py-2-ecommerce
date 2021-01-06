from django.shortcuts import render
from .forms import *

# Create your views here.
def user_login(request):
    context = {}
    context['reg_form'] = UserForm()
    context['details_form'] = CustomerDetailsForm()
    return render(request, 'accounts/login.html', context)
