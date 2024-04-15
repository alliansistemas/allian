# No arquivo forms.py dentro da sua aplicação

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Nome", max_length=30, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']