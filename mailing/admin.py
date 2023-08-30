from django.contrib import admin

from mailing.models import Mailing, Recipient


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('title',)


# @admin.register(Message)
# class MessageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'mailing')


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
