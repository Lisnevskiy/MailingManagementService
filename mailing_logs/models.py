from django.db import models
from django.utils import timezone
from mailing.models import Mailing
from recipient.models import Recipient


class MailingLog(models.Model):
    # Варианты статусов для лога рассылки
    STATUS_SUCCESSFUL = 'successful'
    STATUS_FAILED = 'failed'

    STATUS_CHOICES = [
        (STATUS_SUCCESSFUL, 'Successful'),
        (STATUS_FAILED, 'Failed'),
    ]

    attempt_time = models.DateTimeField(default=timezone.now, verbose_name='Дата и время попытки')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Статус попытки')
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, verbose_name='Получатель')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    error_message = models.TextField(blank=True, null=True, verbose_name='Сообщение об ошибке')

    class Meta:
        verbose_name = 'Лог рассылки'
        verbose_name_plural = 'Логи рассылки'

    def __str__(self):
        return (f'Лог рассылки "{self.mailing}" для {self.recipient}. Время рассылки - {self.attempt_time}, '
                f'статус - {self.status}')
