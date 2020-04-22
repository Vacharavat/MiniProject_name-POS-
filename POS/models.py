
from django.db import models

# Create your models here.

class Product_type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '%s (%s)'%(self.name, self.description)



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50) 
    Type = models.ForeignKey(Product_type, on_delete=models.CASCADE, default='', null=True)
    description = models.CharField(max_length=200, null=False, default='')
    price = models.IntegerField(default=0)

    def __str__(self):
        return '%s (%s)'%(self.name, self.description)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.TimeField()
    total_price = models.FloatField(default=0)
    def __str__(self):
        return '%s (%d)'%(self.date_time, self.total_price)


class Order_Products(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default='', null=True) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='', null=True)
    amount = models.IntegerField(default=0)
    def __str__(self):
        return '%s (%s)'%(self.order, self.product)
