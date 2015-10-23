from django.db import models

# Create your models here.
class Activation(models.Model):
    key = models.CharField(unique=True, max_length=100)
    userid = models.ForeignKey('User', db_column='userId', unique=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='expiryDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Activation'


class Buspass(models.Model):
    buspassid = models.IntegerField(db_column='busPassId', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', db_column='userId', blank=True, null=True)  # Field name made lowercase.
    monthlypass = models.DateTimeField(db_column='monthlyPass', blank=True, null=True)  # Field name made lowercase.
    rides = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BusPass'


class Transactions(models.Model):
    transactionid = models.AutoField(db_column='transactionId', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField()
    gst = models.FloatField()
    pst = models.FloatField()
    cost = models.FloatField()
    total = models.FloatField()
    paymenttype = models.CharField(db_column='paymentType', max_length=45)  # Field name made lowercase.
    userid = models.ForeignKey('User', db_column='userId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transactions'


class User(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    username = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=45)
    registrationdate = models.DateTimeField(db_column='registrationDate')  # Field name made lowercase.
    status = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'User'
