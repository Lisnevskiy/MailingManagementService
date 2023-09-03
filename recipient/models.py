from django.db import models
from django.urls import reverse

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Recipient(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='имя')
    middle_name = models.CharField(max_length=150, verbose_name='отчество', **NULLABLE)
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    email = models.EmailField(unique=True, verbose_name='контактный email')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='отправитель рассылки', **NULLABLE)

    def __str__(self):
        return f'{self.email} ({self.last_name})'

    def get_absolute_url(self):
        return reverse('recipient', kwargs={'recipient_id': self.pk})

    class Meta:
        verbose_name = 'получатель'
        verbose_name_plural = 'получатели'
