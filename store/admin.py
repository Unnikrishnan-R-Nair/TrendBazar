from django.contrib import admin

from store.models import Category, Product, Brand, Size

# Register your models here.

admin.site.register(Category)

admin.site.register(Brand)

admin.site.register(Size)

admin.site.register(Product)