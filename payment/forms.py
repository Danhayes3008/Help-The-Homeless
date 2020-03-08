from django import forms
from.models import Details
# This form tells stripe what card to charge
class MakePaymentForm(forms.Form):
    MONTH_CHOICE = [(i, i) for i in range(1, 12)]
    YEAR_CHOICE = [(i, i) for i in range(2017, 2036)]
    
    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label="Security code", required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICE, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICE, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

# This form deals with address where the users receives the gift from there donation  
class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ('street_address_1', 'street_address_2', 'town_or_city','county', 'postcode', 'country')