from django.core.mail import send_mail
from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

from myproject import settings


class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # Заголовок
    content = models.TextField()  # Содержимое
    preview_image = models.ImageField(upload_to='blog_previews/', blank=True, null=True)  # Превью (изображение)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    is_published = models.BooleanField(default=False)  # Признак публикации
    view_count = models.PositiveIntegerField(default=0)  # Количество просмотров

    def increment_view_count(self):
        self.view_count += 1
        self.save()

    def __str__(self):
        return self.title
