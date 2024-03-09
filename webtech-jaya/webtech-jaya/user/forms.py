# forms.py
from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserSignupForm(BaseUserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='*')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
