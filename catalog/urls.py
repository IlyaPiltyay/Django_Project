from django.urls import path
from . import views
from .views import HomeView, ContactsView, CatalogView, ProductDetailView

app_name = 'catalog'  # устанавливаем пространство имен для приложения

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
]
#  cd C:\Уроки\Django_Project
# python manage.py runserver
