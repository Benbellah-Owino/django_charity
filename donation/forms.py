from django.forms import ModelForm, HiddenInput
from django import forms

from .models import Donation
class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ('amount','charity')

    def __init__(self, *args, **kwargs):
        super(DonationForm, self).__init__(*args, **kwargs)
        # Set the 'charity' field widget to HiddenInput
        self.fields['charity'].widget = HiddenInput()