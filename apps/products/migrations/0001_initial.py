# Generated by Django 4.0.6 on 2022-07-08 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Cadastrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='Tipo de Produto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Cadastrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='Produto')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('home_city', models.CharField(max_length=50, verbose_name='Cidade de Origem')),
                ('availability_date', models.DateField(blank=True, null=True, verbose_name='Data de Disponibilidade')),
                ('type_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_type', to='products.typeproduct', verbose_name='Tipo de Produto')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]