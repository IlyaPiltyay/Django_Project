from django.urls import path
from . import views
from .views import catalog

app_name = 'catalog'  # устанавливаем пространство имен для приложения

urlpatterns = [
    path('home/', views.home, name='home'),  # URL для главной страницы
    path('contacts/', views.contacts, name='contacts'),  # URL для страницы контактов
    path('catalog/', views.catalog, name='catalog'), # URL для страницы товаров
    path('product/<int:id>/', views.product_detail, name='product_detail'), # URL для страницы описания

]
#  cd C:\Уроки\Django_Project
# python manage.py runserver
