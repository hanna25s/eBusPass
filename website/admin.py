from django.contrib import admin
from .models import Activation, Buspass, Transactions, User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('userid', 'username')

class ActivationAdmin(admin.ModelAdmin):
    list_display = ('userid', 'expirydate')

class BuspassAdmin(admin.ModelAdmin):
    list_display = ('buspassid', 'userid')

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('transactionid', 'userid',)

admin.site.register (Activation, ActivationAdmin)
admin.site.register (Buspass, BuspassAdmin)
admin.site.register (Transactions, TransactionsAdmin)
admin.site.register (User, UserAdmin)
