from django import forms
from django.forms import ModelForm

from .models import AuthUser, Name

PASS_TYPES = {
            (1, "10 Rides Youth - $22.00"),
            (2, "10 Rides Adult - $27.00"),
            (3, "Youth Monthly Pass - $60.00"),
            (4, "Post Secondary Monthly Pass - $72.00"),
            (5, "Adult Monthly Pass - $84.00")}


class PurchaseForm(forms.Form):
    pass_type = forms.ChoiceField(choices=PASS_TYPES)
    quantity = forms.IntegerField()


class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = ['first_name', 'last_name']


class UserForm(ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email']
