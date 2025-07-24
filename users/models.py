from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)  # Поле электронной почты как поле для авторизации
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  # Поле для аватара
    phone_number = models.CharField(max_length=15, null=True, blank=True)  # Поле для номера телефона
    country = models.CharField(max_length=50, null=True, blank=True)  # Поле для страны

    USERNAME_FIELD = 'email'  # Указание, что электронная почта является именем пользователя
    REQUIRED_FIELDS = []
