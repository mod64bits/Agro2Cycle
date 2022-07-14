from django.urls import path, re_path
from .views import (ProductListView, ProductCreateView, ListTypeProductView, CreateTypeProductView, UpdateProductView,
                    UploadImageProductWiew)
from apps.core.views import DashBoardView

app_name = "products"

urlpatterns = [
    path('produto/<int:pk>/', UploadImageProductWiew.as_view(), name='products_image_update'),
    path('editar/<slug:slug>/', UpdateProductView.as_view(), name='products_update'),
    path('novo/', ProductCreateView.as_view(), name='products_create'),
    path('lista/', ProductListView.as_view(), name='products_list'),
    path('tipo/', ListTypeProductView.as_view(), name='product_type_list'),
    path('tipo/novo', CreateTypeProductView.as_view(), name='create_product_type'),
]
