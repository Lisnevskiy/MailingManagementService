from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('mailing.urls', namespace='mailing')),
    path('recipients/', include('recipient.urls', namespace='recipient')),
    path('users/', include('users.urls', namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
