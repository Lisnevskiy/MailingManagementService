from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import *

app_name = BlogConfig.name

urlpatterns = [
    path('<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='blogs_detail'),
]
