
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser


class UserLoginForm(AuthenticationForm):
    pass


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].error_messages = {
            'unique': 'Пользователь с таким email уже существует.',
        }
