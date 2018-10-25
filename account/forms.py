from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Password','type':'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Password Confirmacion','type':'password'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2' ,)