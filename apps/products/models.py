from django.db import models
from django.db.models import signals
from apps.core.signals import create_slug


class BaseProduct(models.Model):
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'name'

    class Meta:
        abstract = True


class TypeProduct(BaseProduct):
    name = models.CharField("Tipo de Produto", max_length=50)

    def __str__(self):
        return self.name


signals.post_save.connect(create_slug, sender=TypeProduct)


class Product(BaseProduct):
    name = models.CharField("Produto", max_length=50)
    type_product = models.ForeignKey(
        TypeProduct,
        on_delete=models.CASCADE,
        verbose_name="Tipo",
        related_name="product_type",
        help_text="Tipo de Produto Ex: Café, laranja.."
    )
    description = models.TextField("Descrição")
    home_city = models.CharField("Cidade", max_length=50, help_text="Cidade de Origem Ex: Monte Sião")
    availability_date = models.DateField("Disponibilidade", null=True, blank=True,
                                         help_text="Data que o produto vai está disponível")

    def __str__(self):
        return self.name

    def get_product_info(self):
        return f"Produto: {self.name} Tipo: {self.type_product.name} Disponibilidade: {self.availability_date}"

    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "Produtos"


signals.post_save.connect(create_slug, sender=Product)