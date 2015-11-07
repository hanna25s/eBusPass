from django.shortcuts import render

from django.http import HttpResponse
from .models import UserForm, Transactions, AuthUser
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
	return render(request, 'website/landing_page.html')

@login_required
def purchase_history(request):
	return render(request, 'website/purchase_history.html')

@login_required
def account_info(request):
	form = UserForm()
	return render(request, 'website/account_info.html', {'form':form})

@login_required
def purchase_pass(request):
	return render(request, 'website/purchase_pass.html')

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

@login_required
def paypal_success(request):
	success = "Thank you for your purchase! Your pass has been updated."
	return render(request, 'website/purchase_pass.html', {'success':success})

@login_required
def paypal_notify(request):
	user = AuthUser.objects.get(id=1)
	transaction = Transactions.create(10, "test", user)
	transaction.save()
	return render(request, 'website/purchase_pass.html')

@login_required
def paypal_cancel(request):
	cancel = "Transaction Cancelled"
	return render(request, 'website/purchase_pass.html', {'cancel':cancel})
