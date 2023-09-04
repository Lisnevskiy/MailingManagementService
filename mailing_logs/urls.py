from django.urls import path

from mailing_logs.apps import MailingLogsConfig
from mailing_logs.views import *

app_name = MailingLogsConfig.name

urlpatterns = [
    path('', MailingLogListView.as_view(), name='mailing_logs'),
]
