from django.urls import path
from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),  # Страница входа пользователя.
    path('logout/', UserLogoutView.as_view(), name='logout'),  # Выход пользователя из системы.
    path('register/', UserRegisterView.as_view(), name='register'),  # Регистрация нового пользователя.
    path('profile/', UserUpdateView.as_view(), name='profile'),  # Просмотр и обновление профиля пользователя.
    path('verify/', verify, name='verify'),  # Подтверждение email адреса пользователя после регистрации.
    path('reg_confirmation/', reg_confirmation, name='reg_confirmation'),  # Страница подтверждения успешной регистрации пользователя.
    path('reset_password/', reset_password, name='reset_password'),  # Сброс пароля пользователя.
    path('new_password/', new_password, name='new_password'),  # Создание нового пароля после сброса.
]
