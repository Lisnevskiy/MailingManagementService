from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import *

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailings'),
    path('mailings/<int:pk>/', MailingDetailView.as_view(), name='mailings_detail'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailings_create'),
    path('mailings/update/<int:pk>/', MailingUpdateView.as_view(), name='mailings_update'),
    path('mailings/delete/<int:pk>/', MailingDeleteView.as_view(), name='mailings_delete'),
]
