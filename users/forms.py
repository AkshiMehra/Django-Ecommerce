from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms

class register_form(UserCreationForm):
    email = forms.CharField(max_length=1000)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']