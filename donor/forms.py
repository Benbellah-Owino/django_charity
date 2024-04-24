from django.forms import ModelForm
from django import forms
from .models import Donor


class DonorRegisterForm(ModelForm):
    class Meta:
        model = Donor
        fields = "__all__"

class DonorLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class DonorUpdateForm(forms.Form):
    class Meta:
        model = Donor
        fields = ('email','usernam', 'phone')
