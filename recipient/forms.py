from django import forms

from recipient.models import Recipient


class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'comment')
