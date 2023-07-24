from django.shortcuts import render, redirect
from .models import Product, Contact
from .forms import *

def index(request):
    products = Product.objects.all()

    return render(request, "crud/index.html", context={'products':products})

def create(request):
    forms = ProductForm(request.POST or None)
    if(forms.is_valid()):
        forms.save()
        return redirect('index')
    
    return render(request, "crud/create.html",context={'forms':forms})

def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('index')


def productData(request, id):
    product = Product.objects.get(id=id)
    context  = {'product':product}
    return render(request, 'crud/index.html', context)

def contacts(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(
            name=name,
            email=email,
            message=message
        )
        contact.save()
    return render(request, "crud/contacts.html")