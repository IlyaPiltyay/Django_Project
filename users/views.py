from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import View

from .forms import CustomUserCreationForm
from django.conf import settings


# Create your views here.

class RegisterView(View):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Отправка приветственного письма
            subject = 'Добро пожаловать на наш сайт!'
            message = f'Уважаемый {user.username},\n\nСпасибо за регистрацию на нашем сайте!'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

            return redirect('users:login')  # Перенаправление на страницу входа
        return render(request, 'users/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = 'catalog:home'
