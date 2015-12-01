from django import forms

PASS_TYPES = {
            (1, "10 Rides Youth - $20.00"),
            (2, "10 Rides Adult - $22.50"),
            (3, "Youth Monthly Pass - $55.00"),
            (4, "Post Secondary Monthly Pass - $65.00"),
            (5, "Adult Monthly Pass - $75.00")}

class PurchaseForm(forms.Form):
    pass_type = forms.ChoiceField(choices=PASS_TYPES)
    quantity = forms.IntegerField()
