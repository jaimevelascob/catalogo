from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class signUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class signInFrom(forms.Form):
    username=forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Username"
        }))

    password=forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Password"
        }))