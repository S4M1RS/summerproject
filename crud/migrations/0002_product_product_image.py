# Generated by Django 4.2.3 on 2023-07-22 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
