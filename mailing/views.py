from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from mailing.forms import MailingForm
from mailing.models import Mailing
from mailing.services import send_mailing_task


class MailingListView(ListView):
    """
    Представление для отображения списка рассылок.
    """
    model = Mailing
    extra_context = {'title': 'Рассылки'}


class MailingDetailView(DetailView):
    """
    Представление для отображения деталей рассылки.
    """
    model = Mailing
    extra_context = {'title': 'Рассылка'}


class MailingCreateView(CreateView):
    """
    Представление для создания новой рассылки.
    """
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailings')
    extra_context = {'title': 'Создание рассылки'}

    def form_valid(self, form):
        """
        Обрабатывает данные формы при их валидности.

        Args:
            form (MailingForm): Форма для создания рассылки.

        Returns:
            HttpResponseRedirect: Перенаправляет на страницу со списком рассылок.

        """
        if form.is_valid():
            self.object = form.save(commit=False)  # Сохраняем объект, но не коммитим его пока
            self.object.sender = self.request.user

            # Проверяем, если время начала уже прошло, то отправляем рассылку сразу
            current_time = timezone.now()
            if self.object.mailing_time <= current_time:
                self.object.status = Mailing.STATUS_STARTED

            self.object.save()  # Теперь коммитим объект

            # Теперь добавляем связи с получателями
            form.save_m2m()

            # Если рассылку нужно запустить, то вызываем функцию для отправки
            if self.object.status == Mailing.STATUS_STARTED:
                send_mailing_task(self.object)

        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    """
    Представление для редактирования рассылки.
    """
    model = Mailing
    form_class = MailingForm
    extra_context = {'title': 'Редактирование рассылки'}

    def get_success_url(self):
        return reverse('mailing:mailings_detail', args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    """
    Представление для удаления рассылки.
    """
    model = Mailing
    success_url = reverse_lazy('mailing:mailings')
    extra_context = {'title': 'Удаление рассылки'}
