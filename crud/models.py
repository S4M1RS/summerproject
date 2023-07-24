from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.IntegerField()
    product_image = models.FileField(upload_to='product-image')

    def __str__(self):
        return self.product_name
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name
