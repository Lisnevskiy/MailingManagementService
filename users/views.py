from django.contrib.auth.views import LoginView, LogoutView
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from users.forms import UserRegForm, UserForm
from users.models import User
from users.services import send_verifications_mail, send_new_password_email


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}


class UserLogoutView(LogoutView):
    pass


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegForm
    success_url = reverse_lazy('users:reg_confirmation')
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}

    def form_valid(self, form):
        self.object = form.save()

        verification_url = self.request.build_absolute_uri(
            reverse('users:verify') + f'?key={self.object.verification_key}'
        )

        send_verifications_mail(self.object.email, verification_url)

        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm
    extra_context = {'title': 'Профиль'}

    def get_object(self, queryset=None):
        return self.request.user


def verify(request):
    key = request.GET.get('key')

    try:
        user = User.objects.get(verification_key=key, is_verified=False)
    except User.DoesNotExist:
        raise Http404('Invalid verification key')

    user.is_verified = True
    user.save()

    context = {'title': 'Верификация'}

    return render(request, 'users/verification_success.html', context=context)


def reg_confirmation(request):
    context = {'title': 'Подтверждение регистрации'}
    return render(request, 'users/reg_confirmation.html', context=context)


def reset_password(request):
    context = {'title': 'Сброс пароля'}

    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'users/email_not_found.html', context)

        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()

        send_new_password_email(email, new_password)

        return render(request, 'users/new_password.html', context)

    else:
        return render(request, 'users/reset_password.html', context)


def new_password(request):
    context = {'title': 'Новый пароль'}
    return render(request, 'users/new_password.html', context=context)


def email_not_found(request):
    context = {'title': 'Не найдено'}
    return render(request, 'users/email_not_found.html', context=context)
