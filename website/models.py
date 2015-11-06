# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm


class Buspass(models.Model):
    buspassid = models.AutoField(db_column='busPassId', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', db_column='userId', blank=True, null=True)  # Field name made lowercase.
    monthlypass = models.DateTimeField(db_column='monthlyPass', blank=True, null=True)  # Field name made lowercase.
    rides = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.buspassid)

    class Meta:
        managed = False
        db_table = 'BusPass'
        verbose_name_plural = "Bus Passes"

class Transactions(models.Model):
    transactionid = models.AutoField(db_column='transactionId', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField()
    gst = models.FloatField()
    pst = models.FloatField()
    cost = models.FloatField()
    total = models.FloatField()
    paymenttype = models.CharField(db_column='paymentType', max_length=45)  # Field name made lowercase.
    userid = models.ForeignKey('AuthUser', db_column='userId')  # Field name made lowercase.

    def __str__(self):
        return str(self.transactionid)

    class Meta:
        managed = False
        db_table = 'Transactions'
        verbose_name_plural = 'Transactions'

class AuthUser(models.Model):
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class UserForm(ModelForm):

    class Meta:
        model = AuthUser
        exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined']
