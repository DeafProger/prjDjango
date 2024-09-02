from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.core.mail import send_mail
from .forms import UserRegisterForm
import os, secrets, random, string
from first.settings import EMAIL_HOST_USER
from django.views import View
from .models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Здравствуйте! Перейдите, пожалуйста, по ссылке для подтверждения почты {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)

class PasswordResetView(View):
    form_class = PasswordResetForm
    template_name = "password_reset.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = User.objects.get(email=email)
                new_password = "".join(
                    random.choices(string.ascii_letters + string.digits, k=8)
                )
                user.password = make_password(new_password)
                user.save()

                send_mail(
                    subject="Восстановление пароля",
                    message=f"Ваш новый пароль: {new_password}",
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[email],
                )
                return redirect(reverse("users:login"))
            except User.DoesNotExist:
                form.add_error("email", "Пользователь с таким email не найден")
        return render(request, self.template_name, {"form": form})


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))
