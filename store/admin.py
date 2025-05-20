

from django import forms
# Register your models here.
from django.contrib import admin
from .models import Category, Product, Feature, Brand,  ProductColor,  ProductImage

from django.contrib import admin
from .models import ProductColor
 
 
   
            # اگر شیء جدید است و product در data فرم هست:
      





admin.site.register(ProductColor)

admin.site.register(Product)
admin.site.register(Category)

admin.site.register(Feature)
admin.site.register(Brand)

