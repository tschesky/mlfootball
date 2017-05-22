# _*_ coding: utf-8 _*_
import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Login:", max_length=30)
    email = forms.EmailField(label="Email:")
    password1 = forms.CharField(label="Password:", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repeat Password:", widget=forms.PasswordInput())
    phone = forms.CharField(label="Phone:", max_length=20, required=False)
    log_on = forms.BooleanField(label="Loging after registration:", required=False)

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 == password2:
            return password2
        else:
            raise forms.ValidationError("Hasła się różnią")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Dopuszczalne są tylko cyfry, litery angielskie i _")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Taki użytkownik już istnieje")