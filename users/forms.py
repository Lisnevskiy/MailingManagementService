from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import User


class UserRegForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar')


class UserEmailForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email',)
