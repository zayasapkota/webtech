# forms.py
from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserSignupForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
