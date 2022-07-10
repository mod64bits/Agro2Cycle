from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Product, TypeProduct
from .forms import ProductCreateForm, TypeProductCreateForm
from bootstrap_modal_forms.generic import BSModalCreateView


class ProductListView(ListView):
    model = Product
    context_object_name = "Products"
    template_name = 'products/index.html'
    paginate_by = 25


class ProductCreateView(BSModalCreateView):
    template_name = 'products/create_product.html'
    form_class = ProductCreateForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('products:products_list')


class ListTypeProductView(ListView):
    model = TypeProduct
    context_object_name = "TypesProducts"
    template_name = 'products/list_type_product.html'
    paginate_by = 25


class CreateTypeProductView(BSModalCreateView):
    template_name = 'products/create_type_product.html'
    form_class = TypeProductCreateForm
    success_message = 'Success: Tipo Criado!!.'
    success_url = reverse_lazy('products:product_type_list')
