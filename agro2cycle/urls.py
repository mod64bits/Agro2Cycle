from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from apps.products import urls as products_url
from apps.core import urls as core_urls

urlpatterns = [
    path('', include(core_urls)),
    path('produtos/', include(products_url)),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
