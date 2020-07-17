from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'ROI', 'stock', 'discount')


admin.site.register(Product, ProductAdmin)
