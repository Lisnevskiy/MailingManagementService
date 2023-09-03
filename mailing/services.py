from django.conf import settings
from django.core.mail import send_mail

from mailing.models import Mailing


def send_mailing_task(mailing):
    """
    Отправляет рассылку писем.
    Args:
        mailing (Mailing): Объект Mailing, содержащий информацию о рассылке.
    """
    recipients = mailing.recipient.all()
    subject = mailing.email_subject
    message = mailing.email_body

    for recipient in recipients:
        recipient_email = recipient.email

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient_email],
            fail_silently=False, # Можно настроить обработку ошибок
        )
        print("Sent message")

    mailing.status = Mailing.STATUS_DONE
    mailing.save()
