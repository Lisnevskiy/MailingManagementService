from django.conf import settings
from django.core.mail import send_mail


def send_verifications_mail(email, verification_url):
    send_mail(
        subject='Подтверждение электронной почты',
        message=f'Перейдите по ссылке, чтобы подтвердить свой адрес электронной почты: {verification_url}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )


def send_new_password_email(email, new_password):
    message = f'Ваш новый пароль для авторизации {new_password}'

    send_mail(
        subject='New Password',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
