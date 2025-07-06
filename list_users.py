import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth.models import User

users = User.objects.all()
for user in users:
    print(f'Username: {user.username}, Email: {user.email}, Superuser: {user.is_superuser}')
