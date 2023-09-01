from django.urls import path

from recipient.apps import RecipientConfig
from recipient.views import *

app_name = RecipientConfig.name

urlpatterns = [
    path('', RecipientListView.as_view(), name='recipients'),
    path('<int:pk>/', RecipientDetailView.as_view(), name='recipients_detail'),
    path('create/', RecipientCreateView.as_view(), name='recipients_create'),
    path('update/<int:pk>/', RecipientUpdateView.as_view(), name='recipients_update'),
    path('delete/<int:pk>/', RecipientDeleteView.as_view(), name='recipients_delete'),
]
