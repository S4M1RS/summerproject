from django.shortcuts import render, redirect
from .models import Product
from .forms import *

def index(request):
    products = Product.objects.all()

    return render(request, "crud/index.html", context={'products':products})

# Create your views here.

def create(request):
    forms = ProductForm(request.POST or None)
    if(forms.is_valid()):
        forms.save()
        return redirect('index')
    
    return render(request, "crud/create.html",context={'forms':forms})
