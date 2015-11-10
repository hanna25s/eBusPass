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

    @classmethod
    def create(cls, cost, paymenttype, userid):
        transaction = cls(cost=cost, paymenttype=paymenttype,gst=cost*0.05,pst=cost*0.05,total=cost*0.1+cost, userid=userid)
        return transaction

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

class PaypalIpn(models.Model):
    business = models.CharField(max_length=127)
    charset = models.CharField(max_length=255)
    custom = models.CharField(max_length=255)
    notify_version = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    parent_txn_id = models.CharField(max_length=19)
    receiver_email = models.CharField(max_length=254)
    receiver_id = models.CharField(max_length=255)
    residence_country = models.CharField(max_length=2)
    test_ipn = models.IntegerField()
    txn_id = models.CharField(max_length=255)
    txn_type = models.CharField(max_length=255)
    verify_sign = models.CharField(max_length=255)
    address_country = models.CharField(max_length=64)
    address_city = models.CharField(max_length=40)
    address_country_code = models.CharField(max_length=64)
    address_name = models.CharField(max_length=128)
    address_state = models.CharField(max_length=40)
    address_status = models.CharField(max_length=255)
    address_street = models.CharField(max_length=200)
    address_zip = models.CharField(max_length=20)
    contact_phone = models.CharField(max_length=20)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    payer_business_name = models.CharField(max_length=127)
    payer_email = models.CharField(max_length=127)
    payer_id = models.CharField(max_length=13)
    auth_amount = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    auth_exp = models.CharField(max_length=28)
    auth_id = models.CharField(max_length=19)
    auth_status = models.CharField(max_length=255)
    exchange_rate = models.DecimalField(max_digits=64, decimal_places=16, blank=True, null=True)
    invoice = models.CharField(max_length=127)
    item_name = models.CharField(max_length=127)
    item_number = models.CharField(max_length=127)
    mc_currency = models.CharField(max_length=32)
    mc_fee = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    mc_gross = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    mc_handling = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    mc_shipping = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    memo = models.CharField(max_length=255)
    num_cart_items = models.IntegerField(blank=True, null=True)
    option_name1 = models.CharField(max_length=64)
    option_name2 = models.CharField(max_length=64)
    payer_status = models.CharField(max_length=255)
    payment_date = models.DateTimeField(blank=True, null=True)
    payment_gross = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    payment_status = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    pending_reason = models.CharField(max_length=255)
    protection_eligibility = models.CharField(max_length=255)
    quantity = models.IntegerField(blank=True, null=True)
    reason_code = models.CharField(max_length=255)
    remaining_settle = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    settle_amount = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    settle_currency = models.CharField(max_length=32)
    shipping = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    shipping_method = models.CharField(max_length=255)
    tax = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    transaction_entity = models.CharField(max_length=255)
    auction_buyer_id = models.CharField(max_length=64)
    auction_closing_date = models.DateTimeField(blank=True, null=True)
    auction_multi_item = models.IntegerField(blank=True, null=True)
    for_auction = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    amount_per_cycle = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    initial_payment_amount = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    next_payment_date = models.DateTimeField(blank=True, null=True)
    outstanding_balance = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    payment_cycle = models.CharField(max_length=255)
    period_type = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    profile_status = models.CharField(max_length=255)
    recurring_payment_id = models.CharField(max_length=255)
    rp_invoice_id = models.CharField(max_length=127)
    time_created = models.DateTimeField(blank=True, null=True)
    amount1 = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    amount2 = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    amount3 = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    mc_amount1 = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    mc_amount2 = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    mc_amount3 = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    password = models.CharField(max_length=24)
    period1 = models.CharField(max_length=255)
    period2 = models.CharField(max_length=255)
    period3 = models.CharField(max_length=255)
    reattempt = models.CharField(max_length=1)
    recur_times = models.IntegerField(blank=True, null=True)
    recurring = models.CharField(max_length=1)
    retry_at = models.DateTimeField(blank=True, null=True)
    subscr_date = models.DateTimeField(blank=True, null=True)
    subscr_effective = models.DateTimeField(blank=True, null=True)
    subscr_id = models.CharField(max_length=19)
    username = models.CharField(max_length=64)
    case_creation_date = models.DateTimeField(blank=True, null=True)
    case_id = models.CharField(max_length=255)
    case_type = models.CharField(max_length=255)
    receipt_id = models.CharField(max_length=255)
    currency_code = models.CharField(max_length=32)
    handling_amount = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    transaction_subject = models.CharField(max_length=255)
    ipaddress = models.CharField(max_length=39, blank=True, null=True)
    flag = models.IntegerField()
    flag_code = models.CharField(max_length=16)
    flag_info = models.TextField()
    query = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    from_view = models.CharField(max_length=6, blank=True, null=True)
    mp_id = models.CharField(max_length=128, blank=True, null=True)

    def get_pass_type(self):
        if "option_selection1=Post+Secondary" in self.query:
            return "Post Secondary"
        elif "option_selection1=Adult" in self.query:
            return "Adult"
        elif "option_selection1=Youth" in self.query:
            return "Youth"
        else:
            return ""

    class Meta:
        managed = False
        db_table = 'paypal_ipn'
