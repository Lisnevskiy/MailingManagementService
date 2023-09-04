from django.db import models
from django.urls import reverse
from users.models import User

# Определение словаря NULLABLE для использования его в полях с опцией blank и null
NULLABLE = {'blank': True, 'null': True}


class Recipient(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='имя')  # Имя получателя
    middle_name = models.CharField(max_length=150, verbose_name='отчество', **NULLABLE)  # Отчество (необязательное)
    last_name = models.CharField(max_length=150, verbose_name='фамилия')  # Фамилия получателя
    email = models.EmailField(unique=True, verbose_name='контактный email')  # Уникальный email получателя
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)  # Комментарий к получателю (необязательный)

    # Связь с пользователем, который добавил данного получателя
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='отправитель рассылки', **NULLABLE)

    # Метод для строкового представления объекта Recipient
    def __str__(self):
        return f'{self.email} ({self.last_name})'

    # Метод для получения абсолютного URL объекта Recipient
    def get_absolute_url(self):
        return reverse('recipient', kwargs={'recipient_id': self.pk})

    class Meta:
        verbose_name = 'получатель'  # Отображаемое имя модели в административной панели Django
        verbose_name_plural = 'получатели'  # Отображаемое имя во множественном числе
