from django import forms
from django.contrib.auth.forms import  UserCreationForm

from .models import CustomUser


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'avatar', 'phone_number', 'country']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email уже используется.")
        return email


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Пароль")


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

