# Generated by Django 4.2.3 on 2023-07-22 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.FileField(upload_to='product-image'),
        ),
    ]