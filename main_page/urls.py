from django.urls import path

from main_page.apps import MainPageConfig
from main_page.views import main_page

app_name = MainPageConfig.name

urlpatterns = [
    path('', main_page, name='main_page'),
]
