# Generated by Django 4.2.3 on 2023-07-24 09:27

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]