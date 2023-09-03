from django.contrib import admin

from mailing_logs.models import MailingLog


@admin.register(MailingLog)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('attempt_time', 'recipient', 'status', 'attempt_time')
