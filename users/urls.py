from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView

app_name = 'users'  # Объявление пространства имён

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),  # Убедитесь, что путь к шаблону корректен
    path('logout/', LogoutView.as_view(next_page='catalog:home'), name='logout'),  # Прямое перенаправление после выхода
    path('register/', RegisterView.as_view(), name='register'),  # Регистрация
]