from django.views.generic import ListView

from mailing_logs.models import MailingLog


class MailingLogListView(ListView):
    model = MailingLog
    extra_context = {'title': 'Логи рассылок'}
