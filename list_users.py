import os
import django

# Строка должна соответствовать вашему проекту
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')  # Измените на ваш проект
django.setup()

from users.models import CustomUser  # Замените 'users' на имя вашего приложения

users = CustomUser.objects.all()
if users.exists():
    for user in users:
        print(f'Username: {user.username}, Email: {user.email}, Superuser: {user.is_superuser}')
else:
    print("No users found.")

superusers = CustomUser.objects.filter(is_superuser=True)

if superusers.exists():
    print("Список суперпользователей:")
    for user in superusers:
        print(f'Username: {user.username}, Email: {user.email}, Superuser: {user.is_superuser}')
else:
    print("Суперпользователи не найдены.")