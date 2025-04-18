from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .settings import STATIC_URL, STATIC_ROOT

handler404 = 'apps.page.views.redirect_to_home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.page.urls', namespace='page')),
]

if settings.DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)