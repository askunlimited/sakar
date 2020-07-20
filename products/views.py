from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import Product
from .forms import *



def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)


def uploads(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('uploads/')

    context = {'form':form}
    return render(request, 'uploads.html', context)