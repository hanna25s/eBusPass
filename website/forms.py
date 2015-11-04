from django import forms

class UpdateAccountInformationForm(forms.Form):
    current_name = forms.CharField(label='Name', max_length=255)

PASS_CHOICES = [("Monthly","Rides")]

class PurchasePassForm(forms.Form):
    pass_types = forms.MultipleChoiceField(required=True,
        widget=forms.RadioSelect, choices=PASS_CHOICES)
    month_amount = forms.IntegerField(required=True, label="Number of Months")
    ride_amount = forms.IntegerField(required=True, label="Number of Rides")
