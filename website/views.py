from django.shortcuts import render

from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.core.urlresolvers import reverse

from .models import UserForm, NameForm, Name, AuthUser, PaypalIpn, Buspass
from .forms import PurchaseForm

from django.utils import timezone
import datetime
import logging
import braintree

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
	return render(request, 'website/landing_page.html')

@login_required
def checkout(request):
	if request.method == "POST":
		if request.POST['quantity']  == "":
			error = "You must enter a quantity"
			return reverse("website/purchase_pass.html")

		quantity = float(request.POST['quantity'])

		if (quantity <= 0):
			error = "You must enter a valid quantity"

		pass_type = request.POST['pass_type']
		nonce = request.POST['payment_method_nonce']
		cost = 0

		if pass_type == "1":
			cost = 20.00
		elif pass_type == "2":
			cost = 22.50
		elif pass_type == "3":
			cost = 55.00
		elif pass_type == "4":
			cost = 65.00
		elif pass_type == "5":
			cost = 75.00

		amount = quantity * cost

		result = braintree.Transaction.sale({
    	"amount": str(amount),
    	"payment_method_nonce": nonce,
		    "options": {
        "submit_for_settlement": True
    	}
		})
		context = {"result":result, "nonce":nonce, "cost":cost, "pass_type":pass_type}
		return render(request, 'website/purchase_complete.html', context)
	else:
		return render(request, 'website/purchase_pass.html')
@login_required
def purchase_history(request):
	bus_pass = get_pass(request.user)
	history = PaypalIpn.objects.filter(custom=request.user.id,flag=0).order_by('-payment_date')
	context = {"purchase_history":history, "bus_pass":bus_pass}
	return render(request, 'website/purchase_history.html', context)

@login_required
def purchase_complete(reques):
	return render(request, 'website/purchase_complete.html')

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
	token = braintree.ClientToken.generate()
	form = PurchaseForm()
	context = {"token":token, "form":form}
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

def get_pass(user):
	try:
		bus_pass = Buspass.objects.get(userid=user.id)
		return bus_pass
	except Buspass.DoesNotExist:
		return None
