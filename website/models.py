from django.db import models

# Create your models here.
class Activation(models.Model):
    key = models.CharField(unique=True, max_length=100, verbose_name="Activation Key")
    userid = models.ForeignKey('User', db_column='userId', unique=True)  # Field name made lowercase.
    expirydate = models.DateTimeField(db_column='expiryDate', verbose_name="Expiry Date")  # Field name made lowercase.

    def __str__(self):
        return str(self.userid)

    class Meta:
        managed = False
        db_table = 'Activation'


class Buspass(models.Model):
    buspassid = models.AutoField(db_column='busPassId', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', db_column='userId', blank=True, null=True)  # Field name made lowercase.
    monthlypass = models.DateTimeField(db_column='monthlyPass', blank=True, null=True, verbose_name="Monthly Expiration Date")  # Field name made lowercase.
    rides = models.IntegerField(blank=True, null=True, verbose_name="Rides Remaining")

    def __str__(self):
        return str(elf.buspassid)

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
    paymenttype = models.CharField(db_column='paymentType', max_length=45, verbose_name="Payment Type")  # Field name made lowercase.
    userid = models.ForeignKey('User', db_column='userId')  # Field name made lowercase.

    def __str__(self):
        return str(self.transactionid)

    class Meta:
        managed = False
        db_table = 'Transactions'
        verbose_name_plural = 'Transactions'


class User(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    username = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=45)
    registrationdate = models.DateTimeField(db_column='registrationDate', verbose_name='Registration Date')  # Field name made lowercase.
    status = models.BooleanField(verbose_name="Active")  # This field type is a guess.

    def __str__(self):
        return str(self.userid) + " - " + self.username

    class Meta:
        managed = False
        db_table = 'User'
