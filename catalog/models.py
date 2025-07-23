from django.contrib.auth.models import User
from django.db import models
from django.conf import settings



# Create your models here.

class Category(models.Model):
    """Модель для хранения информации о категории"""
    name = models.CharField(max_length=255, unique=True, verbose_name="Наименование")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='media/', blank=True, null=True, verbose_name="изображение")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="наименование")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='media/', blank=True, null=True, verbose_name="изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата последнего изменения")
    is_published = models.BooleanField(default=False, verbose_name="статус публикации")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name="Создатель")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
