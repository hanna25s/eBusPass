from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'website/account_info.html');

def purchase_history(request):
	return render(request, 'website/purchase_history.html');

def account_info(request):
	return render(request, 'website/account_info.html');

def purchase_pass(request):
        return render(request, 'website/purchase_pass.html');	
def signout(request):
        return render(request, 'website/signout.html');
def confirmation(request):
        return render(request, 'website/confirmation.html');

def registration(request):
        return render(request, 'website/registration.html');

def signin(request):
        return render(request, 'website/signin.html');
        
