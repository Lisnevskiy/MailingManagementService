from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import *

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailings'),
    path('<int:pk>/', MailingDetailView.as_view(), name='mailings_detail'),
    path('create/', MailingCreateView.as_view(), name='mailings_create'),
    path('update/<int:pk>/', MailingUpdateView.as_view(), name='mailings_update'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='mailings_delete'),
]
