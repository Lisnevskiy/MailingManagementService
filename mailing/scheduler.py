from datetime import timedelta
from dateutil.relativedelta import relativedelta
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.db.models import Q

from mailing.models import Mailing
from django.utils import timezone

from mailing.services import send_mailing_task


def start_scheduled_mailings():
    """
    Функция для запуска отложенных рассылок.

    Эта функция будет вызываться периодически по расписанию и отправлять рассылки,
    которые готовы к отправке на текущий момент.

    Периодичность отправки рассылок зависит от настроек каждой рассылки.
    """
    current_time = timezone.now()
    # Фильтруем объекты Mailing, чтобы найти те, которые имеют статус Mailing.STATUS_CREATED
    # или Mailing.STATUS_STARTED и у которых время рассылки меньше или равно текущему времени.
    scheduled_mailings = Mailing.objects.filter(
        Q(status=Mailing.STATUS_CREATED) | Q(status=Mailing.STATUS_STARTED),
        mailing_time__lte=current_time,
    )

    for mailing in scheduled_mailings:
        mailing.status = Mailing.STATUS_STARTED
        mailing.save()
        send_mailing_task(mailing)

        # Обновляем время отправки рассылки в зависимости от периодичности.
        if mailing.periodicity == Mailing.PERIOD_DAILY:
            mailing.mailing_time += timedelta(days=1)
        elif mailing.periodicity == Mailing.PERIOD_WEEKLY:
            mailing.mailing_time += timedelta(weeks=1)
        elif mailing.periodicity == Mailing.PERIOD_MONTHLY:
            # Обновляем на основе месяца (рассылка будет отправлена через месяц).
            mailing.mailing_time += relativedelta(months=1)

        # Учитываем случай, когда день месяца больше 28.
        if mailing.mailing_time.day > 28:
            mailing.mailing_time = mailing.mailing_time.replace(day=1)
            mailing.mailing_time += relativedelta(day=31)

        mailing.save()


scheduler = BackgroundScheduler()
scheduler.add_job(start_scheduled_mailings, CronTrigger(second='0'))
scheduler.start()
print("Scheduler started")
