from django.urls import path, re_path
from .views import ProductListView, ProductCreateView, ListTypeProductView, CreateTypeProductView

app_name = "products"

urlpatterns = [
    path('novo/', ProductCreateView.as_view(), name='products_create'),
    path('lista/', ProductListView.as_view(), name='products_list'),
    path('tipo/', ListTypeProductView.as_view(), name='product_type_list'),
    path('tipo/novo', CreateTypeProductView.as_view(), name='create_product_type'),
]
