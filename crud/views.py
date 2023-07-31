from django.shortcuts import render, redirect
from .models import Product, Contact
from .forms import *


def index(request):
    products = Product.objects.all()
    searchdata = request.GET.get('search')
    if(searchdata is not "" and searchdata is not None):
        product = Product.objects.filter(product_name__icontains=searchdata)
        return render(request, "crud/index.html", context={'products':product})
    return render(request, "crud/index.html", context={'products':products})


def create(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            print("Form is valid")
            print(forms.cleaned_data['product_image'])

            return redirect('techhy:index')
        else:
            print("Form is not valid:", forms.errors)
    else:
        forms = ProductForm()

    return render(request, "crud/create.html", context={'forms': forms})



def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('techhy:index')

def updateProduct(request, id):
    product = Product.objects.get(id=id)
    forms = ProductForm(request.POST or None, instance=product)

    if(forms.is_valid()):
        forms.save()
        return redirect('techhy:index')

    return render(request,"crud/create.html",{'forms':forms})



def productData(request, id):
    product = Product.objects.get(id=id)
    context  = {'product':product}
    return render(request, 'crud/product.html', context)

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

