from django.db import models

# Create your models here.
class Product_list(models.Model):
    FOOD = 'FD'
    DRINK = 'DK'
    SNACK = 'SK'
    PRODUCT_IN_PASHOP = [
        (FOOD, 'อาหาร'),
        (DRINK, 'เครื่องดื่ม'),
        (SNACK, 'ขนม'),
    ]
    product_name = models.CharField(max_length=100)
    product_in_pa = models.CharField(
        max_length=2,
        choices=PRODUCT_IN_PASHOP,
        default=FOOD,
    )
    product_price = models.IntegerField(default=0)