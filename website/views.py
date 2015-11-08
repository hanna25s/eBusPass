from django.shortcuts import render

from django.http import HttpResponse
from .models import UserForm, Transactions, AuthUser
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

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
	current_user = request.user
	ten_rides = {
		"business": settings.PAYPAL_RECEIVER_EMAIL,
		"amount": "24.50",
		"item_name": "10 Rides",
		"notify_url": "http://54.84.253.83/purchase_pass/notify/",
		"return_url": "http://54.84.253.83/purchase_pass/success/",
		"cancel_return": "http://54.84.253.83/purchase_pass/cancel/",
		"undefined_quantity":1,
		"custom":current_user.id
	}
	monthly = {
		"business": settings.PAYPAL_RECEIVER_EMAIL,
		"item_name": "Monthly Pass",
		"notify_url": "http://54.84.253.83/purchase_pass/notify/",
		"return_url": "http://54.84.253.83/purchase_pass/success/",
		"cancel_return": "http://54.84.253.83/purchase_pass/cancel/",
		"undefined_quantity":1,
		"on0":"Monthly",
		"os0":"Pass Type",
		"option_select0":"Youth",
		"option_amount0":55,
		"option_select1":"Post Secondary",
		"option_amount1":65,
		"option_select2":"Adult",
		"option_amount2":75,
		"currency_code":"CAD",
		"custom":current_user.id
	}

	per_ride_form = PayPalPaymentsForm(initial=ten_rides)
	monthly_form = PayPalPaymentsForm(initial=monthly)
	context = {"per_ride_form":per_ride_form, "monthly_form":monthly_form}
	return render(request, 'website/purchase_pass.html', context)

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

@csrf_exempt
@login_required
def paypal_success(request):
	success = "Thank you for your purchase! Your pass has been updated."
	return render(request, 'website/purchase_pass.html', {'success':success})

@login_required
def paypal_cancel(request):
	cancel = "Transaction Cancelled"
	return render(request, 'website/purchase_pass.html', {'cancel':cancel})
