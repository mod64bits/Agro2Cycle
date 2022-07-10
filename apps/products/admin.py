from django.contrib import admin
from .models import Product


class ProductsAdmin(admin.ModelAdmin):
    fields = ("type_product", "name", "home_city", "availability_date", "description",)



admin.site.register(Product, ProductsAdmin)