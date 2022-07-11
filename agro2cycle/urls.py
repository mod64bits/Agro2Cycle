from django.contrib import admin
from django.urls import path, include

from apps.products import urls as products_url
from apps.core import urls as core_urls

urlpatterns = [
    path('', include(core_urls)),
    path('produtos', include(products_url)),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]
