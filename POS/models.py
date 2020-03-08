from django.db import models


# Create your models here.
class product_type(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True)



class product(models.Model):
    name = models.CharField(max_length=50) 
    product_type = models.ForeignKey(product_type, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True)
    price = models.IntegerField()
