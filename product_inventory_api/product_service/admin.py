from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    list_filter = ('category', 'price') 
    search_fields = ['name']
    ordering = ('category', 'name', 'price', 'quantity')
    list_per_page = 10

# Register your models here.
admin.site.register(Product, ProductAdmin)