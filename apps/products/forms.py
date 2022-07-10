from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Product, TypeProduct


class DateInput(forms.DateInput):
    input_type = 'date'


class ProductCreateForm(BSModalModelForm):
    availability_date = forms.DateField(label="Previsão", widget=DateInput)

    class Meta:
        model = Product
        fields = '__all__'


class TypeProductCreateForm(BSModalModelForm):
    class Meta:
        model = TypeProduct
        fields = '__all__'
