from django.contrib.auth.views import LoginView

from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import CustomUserCreationForm
from django.conf import settings


# Create your views here.

class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()

        subject = 'Добро пожаловать на наш сайт!'
        message = f'Уважаемый пользователь,\n\nСпасибо за регистрацию на нашем сайте!'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = 'catalog:home'
