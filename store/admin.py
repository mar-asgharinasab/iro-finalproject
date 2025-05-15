

# Register your models here.
from django.contrib import admin
from .models import Category, Product, Feature, Brand

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Feature)
admin.site.register(Brand)