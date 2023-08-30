from django.urls import path

from users.apps import UsersConfig
from users.views import UserLoginView, UserLogoutView, UserRegisterView, verify, reg_confirmation, reset_password, \
    new_password, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('verify/', verify, name='verify'),
    path('reg_confirmation/', reg_confirmation, name='reg_confirmation'),
    path('reset_password/', reset_password, name='reset_password'),
    path('new_password/', new_password, name='new_password'),
    # path('permission_denied/', permission_denied, name='permission_denied'),
]
