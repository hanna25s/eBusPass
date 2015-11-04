from django.shortcuts import render

from django.http import HttpResponse
from .forms import PurchasePassForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	return render(request, 'website/landing_page.html')

@login_required
def purchase_history(request):
	return render(request, 'website/purchase_history.html')

@login_required
def account_info(request):
	return render(request, 'website/account_info.html')

@login_required
def purchase_pass(request):
	form = PurchasePassForm()
	return render(request, 'website/purchase_pass.html', {'form':form})

@login_required
def signout(request):
    return render(request, 'website/signout.html')

@login_required
def confirmation(request):
    return render(request, 'website/confirmation.html')

def registration(request):
    return render(request, 'website/registration.html')

def signin(request):
    return render(request, 'website/signin.html')

@login_required
def user_profile(request):
    return render(request, 'website/user_profile.html')
