from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .models import UserForm, NameForm, Name, AuthUser, Buspass, Transactions
from .forms import PurchaseForm

import datetime
from datetime import timedelta
import logging
import braintree

MONTHLY_ADULT_COST = 84.00
MONTHLY_POST_SECONDARY_COST = 72.00
MONTHLY_YOUTH_COST = 60.00

PER_RIDE_ADULT_COST = 27.00
PER_RIDE_YOUTH_COST = 22.00

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
	return render(request, 'website/landing_page.html')

@login_required
def purchase_history(request):
	bus_pass = get_pass(request.user)
	history = Transactions.objects.filter(userid=request.user.id).order_by('-date')
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
	error = ""
	if request.method == "POST":
		form = PurchaseForm(request.POST)
		if not form.is_valid():
			error = "Please complete all fields below"
		else:
			quantity = float(request.POST['quantity'])

			if (quantity <= 0):
				error = "Quantity must be greater than zero"
			else:
				pass_type = request.POST['pass_type']
				nonce = request.POST['payment_method_nonce']
				cost = 0

				if pass_type == "1":
					cost = PER_RIDE_YOUTH_COST
					pass_description = "Per Ride - Youth"
				elif pass_type == "2":
					cost = PER_RIDE_ADULT_COST
					pass_description = "Per Ride - Adult"
				elif pass_type == "3":
					cost = MONTHLY_YOUTH_COST
					pass_description = "Monthly - Youth"
				elif pass_type == "4":
					cost = MONTHLY_POST_SECONDARY_COST
					pass_description = "Monthly - Post Secondary"
				elif pass_type == "5":
					cost = MONTHLY_ADULT_COST
					pass_description = "Monthly - Adult"

				amount = quantity * cost
				user = AuthUser.objects.get(id=request.user.id)

				result = braintree.Transaction.sale({
		    		"amount": str(amount),
		    		"payment_method_nonce": nonce,
				    "options": {
		        		"submit_for_settlement": True
		    		}
				})

				if result.is_success:
					try:
						bus_pass = Buspass.objects.get(userid=user.id)
					except Buspass.DoesNotExist:
						bus_pass = Buspass()
						bus_pass.userid = user
						bus_pass.rides = 0
						bus_pass.monthlypass = None

					if (pass_type == "1" or pass_type == "2"):
						bus_pass.rides += quantity * 10
					elif (pass_type == "3" or pass_type == "4" or pass_type == "5"):
						pass_time = quantity * 31
						#Check to see if the pass is expired or valid. If valid, add to
						#current expiry date. Otherwise, add one month starting today
						if(bus_pass.monthlypass is None or bus_pass.monthlypass <= datetime.date.today()):
							bus_pass.monthlypass = datetime.date.today() + timedelta(days=pass_time)
						else:
							bus_pass.monthlypass += timedelta(days=pass_time)

					bus_pass.save()

					transaction = Transactions()
					transaction.userid = user
					transaction.cost = amount
					transaction.quantity = quantity
					transaction.passtype = pass_description
					transaction.save()

					return render(request, 'website/purchase_complete.html')
				else:
					error = "Purchase Failed"

	token = braintree.ClientToken.generate()
	form = PurchaseForm()
	context = {"token":token, "form":form, "error":error}
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

def generate_token(request):
	if request.method == "GET":
		return HttpResponse(braintree.ClientToken.generate())

@csrf_exempt
def process_nonce(request):
	if request.method == "POST":
		nonce = request.POST['nonce']
		pass_type = request.POST['pass_type']
		quantity = int(request.POST['quantity'])
		amount = request.POST['amount']
		userid = 41

		try:
			user = AuthUser.objects.get(id=userid)
		except Buspass.DoesNotExist:
			return HttpResponse("Invalid User")

		result = braintree.Transaction.sale({
			"amount": str(amount),
			"payment_method_nonce": nonce,
			"options": {
				"submit_for_settlement": True
			}
		})

		if result.is_success:
			try:
				bus_pass = Buspass.objects.get(userid=user.id)
			except Buspass.DoesNotExist:
				bus_pass = Buspass()
				bus_pass.userid = user
				bus_pass.rides = 0
				bus_pass.monthlypass = None

			if (pass_type == "10 Rides - Adult" or pass_type == "10 Rides - Youth"):
				bus_pass.rides += quantity * 10
			elif (pass_type == "Monthly - Youth" or pass_type == "Monthly - Adult" or pass_type == "Monthly - Post Secondary"):
				pass_time = quantity * 31
				#Check to see if the pass is expired or valid. If valid, add to
				#current expiry date. Otherwise, add one month starting today
				if(bus_pass.monthlypass is None or bus_pass.monthlypass <= datetime.date.today()):
					bus_pass.monthlypass = datetime.date.today() + timedelta(days=pass_time)
				else:
					bus_pass.monthlypass += timedelta(days=pass_time)

			bus_pass.save()

			transaction = Transactions()
			transaction.userid = user
			transaction.cost = amount
			transaction.quantity = quantity
			transaction.passtype = pass_type
			transaction.save()

			return HttpResponse("Success")
		else:
			return HttpResponse("Purchase Failed")

	else:
		return HttpResponse("404")

def get_pass(user):
	try:
		bus_pass = Buspass.objects.get(userid=user.id)
		return bus_pass
	except Buspass.DoesNotExist:
		return None
