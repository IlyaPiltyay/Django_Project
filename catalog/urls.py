from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),  # URL для домашней страницы
    path('contacts/', views.contacts, name='contacts'),  # URL для страницы контактов
]

#  cd C:\Уроки\Django_Project
# python manage.py runserver
