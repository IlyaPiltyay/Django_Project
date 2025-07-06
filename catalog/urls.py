from django.urls import path
from . import views
from .views import HomeView, ContactsView, CatalogView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductDetailView

app_name = 'catalog'  # устанавливаем пространство имен для приложения

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/', CatalogView.as_view(), name='catalog'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),



]
#  cd C:\Уроки\Django_Project
# python manage.py runserver
