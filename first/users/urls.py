from django.contrib.auth.views import LoginView
from django.urls import path
from .views import UserCreateView, email_verification, PasswordResetView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', UserCreateView.as_view(template_name='register.html'), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path("password-reset/", PasswordResetView.as_view(), name="password_reset"),
]
