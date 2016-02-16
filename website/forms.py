from django import forms


PASS_TYPES = {
            (1, "10 Rides Youth - $22.00"),
            (2, "10 Rides Adult - $27.00"),
            (3, "Youth Monthly Pass - $60.00"),
            (4, "Post Secondary Monthly Pass - $72.00"),
            (5, "Adult Monthly Pass - $84.00")}

class PurchaseForm(forms.Form):
    pass_type = forms.ChoiceField(choices=PASS_TYPES)
    quantity = forms.IntegerField()
