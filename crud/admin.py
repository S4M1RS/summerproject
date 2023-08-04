from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header="Techhy Ecommerce"
admin.site.site_title="Techhy Admin"
admin.site.index_title=""

class ProductAdmin(admin.ModelAdmin):
    list_display = '__str__','product_name','brand','price','product_image'
    list_editable = 'product_name','brand','price'
    search_fields = 'product_name',

class ContactAdmin(admin.ModelAdmin):
    list_display = '__str__','name','email','message'
    list_editable = 'name','email','message'
    search_fields = 'name',


admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)