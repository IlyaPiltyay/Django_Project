from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Пароль")


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')
