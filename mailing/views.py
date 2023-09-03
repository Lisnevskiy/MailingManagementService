from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from mailing.forms import MailingForm
from mailing.models import Mailing


class MailingListView(ListView):
    model = Mailing
    extra_context = {'title': 'Рассылки'}


class MailingDetailView(DetailView):
    model = Mailing
    extra_context = {'title': 'Рассылка'}


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailings')
    extra_context = {'title': 'Создание рассылки'}

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.sender = self.request.user
            self.object.save()

        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    extra_context = {'title': 'Редактирование рассылки'}

    def get_success_url(self):
        return reverse('mailing:mailings_detail', args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailings')
    extra_context = {'title': 'Удаление рассылки'}
