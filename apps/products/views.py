from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


from .models import Product, TypeProduct, ImagensProducts
from .forms import ProductCreateForm, TypeProductCreateForm, UpdateProductForm, ImagesForm
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


class UpdateProductView(UpdateView):
    model = Product
    form_class = UpdateProductForm
    template_name = 'products/update_product.html'

    def get_imagens(self):
        imagens = ImagensProducts.objects.filter(product=self.object)
        return imagens

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imagens'] = self.get_imagens()
        return context


class ListTypeProductView(ListView):
    model = TypeProduct
    context_object_name = "TypesProducts"
    template_name = 'products/list_type_product.html'
    paginate_by = 25



class CreateTypeProductView(BSModalCreateView):
    template_name = 'products/create_type_product.html'
    form_class = TypeProductCreateForm
    success_message = 'Success: Tipo Criado!!.'
    #success_url = reverse_lazy('products:products_update' self.kwargs)


class UploadImageProductWiew(BSModalCreateView):
    template_name = 'products/upload_image_product.html'
    form_class = ImagesForm
    success_message = 'Success: Tipo Criado!!.'
    success_url = reverse_lazy('products:products_list')

    def post(self, request, *args, **kwargs):
        # TODO: Bug as imagens estão duplicando
        files = request.FILES.getlist('image')
        product = Product.objects.get(pk=kwargs['pk'])
        url = f"/produtos/editar/{product.slug}/"
        for file in files:
            image = ImagensProducts.objects.create(product=product, image=file)
            image.save()
        return redirect(url)




