from django import forms
from django.forms import DateTimeInput

from mailing.models import Mailing


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('title', 'email_subject', 'email_body', 'mailing_time', 'periodicity', 'recipient')
        widgets = {
            'mailing_time': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
