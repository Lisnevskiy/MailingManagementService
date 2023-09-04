from django.conf import settings
from django.core.mail import send_mail


def send_verifications_mail(email, verification_url):
    """
    Отправляет письмо с ссылкой для подтверждения email адреса.
    Args:
        email (str): Email адрес пользователя.
        verification_url (str): URL для подтверждения email адреса.
    """
    send_mail(
        subject='Подтверждение электронной почты',
        message=f'Перейдите по ссылке, чтобы подтвердить свой адрес электронной почты: {verification_url}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )


def send_new_password_email(email, new_password):
    """
    Отправляет письмо с новым паролем.
    Args:
        email (str): Email адрес пользователя.
        new_password (str): Новый пароль пользователя.
    """
    message = f'Ваш новый пароль для авторизации: {new_password}'

    send_mail(
        subject='New Password',
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
