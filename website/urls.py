# This file is for routing URLs

from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^purchase_history/', views.purchase_history),
    url(r'^account_info/^', views.account_info),
]
