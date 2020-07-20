from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import Product
from .forms import *



def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)


def uploads(request):
    products = Product.objects.all()
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'product': products, 'form':form}
    return render(request, 'uploads.html', context)


def updateProducts(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'uploads/update_form.html', context)

