from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^purchase_history/', views.purchase_history),
    url(r'^account_info/', views.account_info),
    url(r'^reg_name/', views.reg_name),
    url(r'^purchase_pass/', views.purchase_pass),
    url(r'^confirmation/', views.confirmation),
    url(r'^signout/', views.signout),
    url(r'^registration/', views.registration),
    url(r'^signin/', views.signin),
    url(r'^user_profile/', views.user_profile),
    url(r'^purchase_complete/', views.purchase_complete),
    url(r'^generate_token/', views.generate_token),
    url(r'^process_nonce/', views.process_nonce),
    url(r'^get_pass_information/', views.get_pass_information),
    url(r'^ride_bus/', views.ride_bus),
    url(r'^sync_pass/', views.sync_pass),
]
