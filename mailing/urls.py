from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import *

app_name = MailingConfig.name

urlpatterns = [
    # Список рассылок
    path('', MailingListView.as_view(), name='mailings'),

    # Детали рассылки
    path('<int:pk>/', MailingDetailView.as_view(), name='mailings_detail'),

    # Создание новой рассылки
    path('create/', MailingCreateView.as_view(), name='mailings_create'),

    # Обновление рассылки
    path('update/<int:pk>/', MailingUpdateView.as_view(), name='mailings_update'),

    # Удаление рассылки
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='mailings_delete'),

    # Изменение статуса рассылки
    path('change_status/<int:pk>/', change_mailing_status, name='change_status'),
]

