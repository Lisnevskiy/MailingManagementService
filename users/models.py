import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Пользовательская модель пользователя с расширенными полями.
    """
    username = None

    email = models.EmailField(verbose_name='почта', unique=True)

    verification_key = models.UUIDField(default=uuid.uuid4, editable=False)
    """
    Уникальный идентификатор пользователя (UUID) для подтверждения аккаунта.
    Автоматически генерируется при создании нового пользователя.
    Не редактируется пользователем.
    """

    is_verified = models.BooleanField(default=False)
    """
    Флаг, который указывает, подтвержден ли аккаунт пользователя.
    По умолчанию устанавливается в False и изменяется на True при подтверждении аккаунта.
    """

    first_name = models.CharField(max_length=150, verbose_name='имя', **NULLABLE)

    last_name = models.CharField(max_length=150, verbose_name='фамилия', **NULLABLE)

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
