from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Donor


class DonorRegisterForm(UserCreationForm):
    class Meta:
        model = Donor
        fields = "__all__"
        exclude = ['last_login', 'groups', 'user_permissions', 'total_donated','password']

class DonorLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class DonorUpdateForm(forms.Form):
    class Meta:
        model = Donor
        fields = ('email','username', 'phone')
