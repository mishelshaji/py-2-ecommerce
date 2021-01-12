from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
@login_required
@user_passes_test(lambda x:x.is_customer)
def home(request):
    return render(request, 'customer/home.html')