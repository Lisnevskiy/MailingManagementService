from django import forms

from mailing.models import Mailing


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ('title', 'email_subject', 'email_body', 'periodicity', 'recipient')
