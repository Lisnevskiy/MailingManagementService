from django.db import models
from django.urls import reverse

from recipient.models import Recipient
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Mailing(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
        (PERIOD_MONTHLY, 'Раз в месяц'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'

    STATUSES = (
        (STATUS_CREATED, 'Создана'),
        (STATUS_STARTED, 'Запущена'),
        (STATUS_DONE, 'Завершена'),
    )

    title = models.CharField(max_length=250, verbose_name='название рассылки')
    email_subject = models.CharField(max_length=250, verbose_name='тема письма')
    email_body = models.TextField(verbose_name='содержание письма')
    mailing_time = models.DateTimeField(auto_now=True, verbose_name='время рассылки')
    periodicity = models.CharField(max_length=20, choices=PERIODS, verbose_name='периодичность')
    status = models.CharField(max_length=20, choices=STATUSES, default=STATUS_CREATED, verbose_name='статус рассылки')

    recipient = models.ManyToManyField(Recipient, verbose_name='получатель', related_name='mailing')

    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='отправитель рассылки', **NULLABLE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mailing', kwargs={'mailing_id': self.pk})

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
