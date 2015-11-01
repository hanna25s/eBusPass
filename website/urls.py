# This file is for routing URLs

from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^purchase_history/', views.purchase_history),
    url(r'^account_info/', views.account_info),
    url(r'^purchase_pass/', views.purchase_pass),
    url(r'^confirmation/', views.confirmation),
    url(r'^signout/', views.signout),
    url(r'^registration/', views.registration),
    url(r'^signin/', views.signin),
    url(r'^user_profile/', views.user_profile),

]
