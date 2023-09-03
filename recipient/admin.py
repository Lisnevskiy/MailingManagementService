from django.contrib import admin

from recipient.models import Recipient


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
