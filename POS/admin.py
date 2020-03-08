from django.contrib import admin
from POS.models import product_type, product
# Register your models here.

admin.site.register(product_type)
admin.site.register(product)
