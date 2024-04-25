from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Owner, Charity


class OwnerRegisterForm(UserCreationForm):
    class Meta:
        model = Owner
        fields = "__all__"
        exclude = ['last_login', 'groups', 'user_permissions', 'password']


class OwnerLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class OwnerUpdateForm(forms.Form):
    class Meta:
        model = Owner
        fields = ('email', 'username', 'phone')


class CharityCreateForm(forms.ModelForm):
    class Meta:
        model = Charity
        fields = ('name', 'description', 'phone_number', 'address', 'website', 'mission')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Charity Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone number'


class CharityUpdateForm(forms.ModelForm):
    class Meta:
        model = Charity
        fields = ['name', 'description', 'phone_number', 'address', 'website', 'logo', 'mission']