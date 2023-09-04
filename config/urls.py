from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main_page.urls', namespace='main_page')),
    path('mailings/', include('mailing.urls', namespace='mailing')),
    path('mailing_logs/', include('mailing_logs.urls', namespace='mailing_log')),
    path('recipients/', include('recipient.urls', namespace='recipient')),
    path('blogs/', include('blog.urls', namespace='blog')),
    path('users/', include('users.urls', namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
