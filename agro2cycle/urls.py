from django.contrib import admin
from django.urls import path, include

from apps.products import urls as products_url

urlpatterns = [
    path('produtos/', include(products_url)),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]
