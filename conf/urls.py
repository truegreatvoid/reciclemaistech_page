from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .settings import STATIC_URL, STATIC_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.page.urls', namespace='page')),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)