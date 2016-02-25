from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm


class Buspass(models.Model):
    buspassid = models.AutoField(db_column='busPassId', primary_key=True)
    userid = models.ForeignKey('AuthUser', db_column='userId',
                               blank=True, null=True)
    monthlypass = models.DateTimeField(db_column='monthlyPass',
                                       blank=True, null=True)
    rides = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.buspassid)

    class Meta:
        managed = False
        db_table = 'BusPass'
        verbose_name_plural = "Bus Passes"


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

    def __str__(self):
        return str(self.id) + ' - ' + self.username

    class Meta:
        managed = False
        db_table = 'auth_user'


class Name(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name

    class Meta:
        managed = False
        db_table = 'auth_user'


class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = ['first_name', 'last_name']


class UserForm(ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email']


class Transactions(models.Model):
    transactionid = models.AutoField(db_column='transactionId',
                                     primary_key=True)
    date = models.DateTimeField()
    cost = models.FloatField()
    userid = models.ForeignKey('AuthUser', db_column='userId')
    passtype = models.CharField(max_length=45)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Transactions'
        verbose_name_plural = "Transactions"
