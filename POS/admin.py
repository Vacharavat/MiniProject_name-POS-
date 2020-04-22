from django.contrib import admin
from django.contrib.auth.models import Permission
from POS.models import Product_type, Product, Order, Order_Products
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


class OrderAdmin(admin.ModelAdmin):
    list_display = ['date_time', 'total_price']
    list_per_page = 10
    list_filter = ['date_time']
    search_fields = ['date_time']

admin.site.register(Order, OrderAdmin)


class Order_ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'amount']
    list_per_page = 10
    list_filter = ['product_id']
    search_fields = ['product_id']



admin.site.register(Order_Products, Order_ProductsAdmin)

admin.site.register(Permission)