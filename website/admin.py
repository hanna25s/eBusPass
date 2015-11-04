from django.contrib import admin
from .models import Buspass, Transactions
# Register your models here.

class BuspassAdmin(admin.ModelAdmin):
    list_display = ('buspassid', 'userid')

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('transactionid', 'userid',)

admin.site.register (Buspass, BuspassAdmin)
admin.site.register (Transactions, TransactionsAdmin)
