from django.contrib import admin
from .models import Buspass
# Register your models here.

class BuspassAdmin(admin.ModelAdmin):
    list_display = ('buspassid', 'userid')

admin.site.register (Buspass, BuspassAdmin)
