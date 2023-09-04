from django import forms
from django.forms import DateTimeInput, CheckboxSelectMultiple
from mailing.models import Mailing
from recipient.models import Recipient


class MailingForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        """
        Инициализация формы для создания рассылки.

        Args:
            user (User): Пользователь, создающий рассылку.
            *args: Позиционные аргументы для передачи в конструктор родительской формы.
            **kwargs: Именованные аргументы для передачи в конструктор родительской формы.
        """
        super(MailingForm, self).__init__(*args, **kwargs)

        # Фильтрация получателей на основе пользователя
        if user:
            self.fields['recipient'].queryset = Recipient.objects.filter(sender=user)

    recipient = forms.ModelMultipleChoiceField(
        queryset=Recipient.objects.none(),  # Пустой queryset, он будет переопределен в __init__
        widget=CheckboxSelectMultiple,
        required=False,
        label='Получатели'
    )

    class Meta:
        model = Mailing
        fields = ('title', 'email_subject', 'email_body', 'mailing_time', 'periodicity', 'recipient')
        widgets = {
            'mailing_time': DateTimeInput(attrs={'type': 'datetime-local'}),
        }
