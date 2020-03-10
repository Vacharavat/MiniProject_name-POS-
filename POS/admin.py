from django.contrib import admin
from POS.models import Product_type, Product
# Register your models here.


class Product_TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Product_type, Product_TypeAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price']
    list_per_page = 10
    list_filter = ['name', 'price']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
