from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.signals import request_finished
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from paypal.standard.forms import PayPalPaymentsForm

from .models import UserForm, NameForm, Name, AuthUser, PaypalIpn, Buspass


from django.utils import timezone
import datetime
import logging
logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
	return render(request, 'website/landing_page.html')

@login_required
def purchase_history(request):
	history = PaypalIpn.objects.filter(custom=request.user.id).order_by('-payment_date')
	context = {"purchase_history":history}
	return render(request, 'website/purchase_history.html', context)

@login_required
def reg_name(request):
	k=request.user.id
	a = Name.objects.get(pk=k)
	f = NameForm(request.POST,instance=a)
	if f.is_valid():
		f.save()
		return render(request,'website/user_profile.html')
	else:
		form = NameForm(instance=a)
		return render(request, 'website/reg_name.html', {'form':form})

@login_required
def account_info(request):


	#if request.method == "POST":
	k=request.user.id
	a = AuthUser.objects.get(pk=k)
	f = UserForm(request.POST,instance=a)
	if f.is_valid():
		f.save()
		return render(request,'website/user_profile.html')
	else:
		form = UserForm(instance=a)
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
		"custom":current_user.id,
		"currency_code":"CAD",
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

@receiver(valid_ipn_received)
def update_pass(sender, **kwargs):

	ipn_obj = sender
	quantity = ipn_obj.quantity

	if ipn_obj.payment_status == ST_PP_COMPLETED:
		user = AuthUser.objects.get(id=ipn_obj.custom)
		if(not user):
			return -1

		try:
			bus_pass = Buspass.objects.get(userid=user.id)
		except Buspass.DoesNotExist:
			bus_pass = Buspass()
			bus_pass.userid = user
			bus_pass.rides = 0
			bus_pass.monthlypass = None

		if (ipn_obj.item_name == "10 Rides"):
			bus_pass.rides += quantity * 10
		elif (ipn_obj.item_name == "Monthly Pass"):
			pass_time = datetime.timedelta(quantity*365/12)
			if(bus_pass.monthlypass is None or
			bus_pass.monthlypass <= timezone.make_aware(datetime.datetime.now(), timezone.get_current_timezone())):
				bus_pass.monthlypass = datetime.datetime.now() + pass_time
			else:
				bus_pass.monthlypass += pass_time
		bus_pass.save()
