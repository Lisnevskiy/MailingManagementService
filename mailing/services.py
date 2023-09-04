from django.conf import settings
from django.core.mail import send_mail

from mailing.models import Mailing
from mailing_logs.models import MailingLog


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

        # Отправление письма
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[recipient_email],
                fail_silently=False,
            )

            # Если письмо отправлено успешно, создается запись в логах рассылок
            log = MailingLog(
                mailing=mailing,
                recipient=recipient,
                status=MailingLog.STATUS_SUCCESSFUL,  # Успешно доставлено
            )
            log.save()

        except Exception as e:
            # Если произошла ошибка при отправке письма, создается запись в логах с ошибкой
            log = MailingLog(
                mailing=mailing,
                recipient=recipient,
                status=MailingLog.STATUS_FAILED,  # Ошибка доставки
                error_message=str(e),  # Сохраняется сообщение об ошибке
            )
            log.save()

    # mailing.status = Mailing.STATUS_DONE
    mailing.save()
