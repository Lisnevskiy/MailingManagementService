from django.urls import path

from blog.apps import BlogConfig
from blog.views import *

app_name = BlogConfig.name

urlpatterns = [
    path('<int:pk>/', BlogDetailView.as_view(), name='blogs_detail'),
]
