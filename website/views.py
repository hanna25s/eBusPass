from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'website/index.html');

def purchase_history(request):
	return render(request, 'website/purchase_history.html');

def account_info(request):
	return render(request, 'website/account_info.html');

