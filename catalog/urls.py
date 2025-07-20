from django.urls import path
from .views import (CatalogView, ContactsView, HomeView, ProductCreateView,
                    ProductDeleteView, ProductDetailView, ProductListView,
                    ProductUpdateView)

app_name = 'catalog'  # устанавливаем пространство имен для приложения

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

]
#  cd C:\Уроки\Django_Project
# python manage.py runserver
