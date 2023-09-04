from django.urls import path
from recipient.apps import RecipientConfig
from recipient.views import *

# Получаем имя приложения "recipient" из его конфигурации
app_name = RecipientConfig.name

urlpatterns = [
    # Маршрут для отображения списка получателей
    path('', RecipientListView.as_view(), name='recipients'),

    # Маршрут для отображения деталей конкретного получателя
    path('<int:pk>/', RecipientDetailView.as_view(), name='recipients_detail'),

    # Маршрут для создания нового получателя
    path('create/', RecipientCreateView.as_view(), name='recipients_create'),

    # Маршрут для редактирования существующего получателя
    path('update/<int:pk>/', RecipientUpdateView.as_view(), name='recipients_update'),

    # Маршрут для удаления существующего получателя
    path('delete/<int:pk>/', RecipientDeleteView.as_view(), name='recipients_delete'),
]
