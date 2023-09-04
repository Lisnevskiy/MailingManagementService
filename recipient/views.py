from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from recipient.forms import RecipientForm
from recipient.models import Recipient


class RecipientListView(ListView):
    """
    Представление для отображения списка получателей.
    """
    model = Recipient
    extra_context = {'title': 'Получатели'}


class RecipientDetailView(DetailView):
    """
    Представление для отображения деталей конкретного получателя.
    """
    model = Recipient
    extra_context = {'title': 'Получатель'}


class RecipientCreateView(LoginRequiredMixin, CreateView):
    """
    Представление для создания нового получателя.
    """
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('recipient:recipients')
    extra_context = {'title': 'Добавление получателя'}

    def form_valid(self, form):
        """
        Обрабатывает данные формы при их валидности.
        """
        if form.is_valid():
            self.object = form.save()
            self.object.sender = self.request.user
            self.object.save()
        return super().form_valid(form)


class RecipientUpdateView(UpdateView):
    """
    Представление для редактирования существующего получателя.
    """
    model = Recipient
    form_class = RecipientForm
    extra_context = {'title': 'Редактирование получателя'}

    def get_success_url(self):
        return reverse('mailing:mailings_detail', args=[self.kwargs.get('pk')])


class RecipientDeleteView(DeleteView):
    """
    Представление для удаления существующего получателя.
    """
    model = Recipient
    success_url = reverse_lazy('recipient:recipients')
    extra_context = {'title': 'Удаление получателя'}
