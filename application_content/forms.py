# _*_ coding: utf-8 _*_
from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Login:", max_length=30)
    email = forms.EmailField(label="Email:")
    password1 = forms.CharField(label="Password:", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repeat Password:", widget=forms.PasswordInput())
    phone = forms.CharField(label="Phone:", max_length=20, required=False)
    log_on = forms.BooleanField(label="Loging after registration:", required=False)
