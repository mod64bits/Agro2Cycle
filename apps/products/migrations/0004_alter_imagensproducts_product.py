# Generated by Django 4.0.6 on 2022-07-13 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_imagensproducts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagensproducts',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='img_product', to='products.product'),
        ),
    ]
