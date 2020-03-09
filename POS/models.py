from django.db import models

# Create your models here.

class product_type(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '%s (%s)'%(self.name, self.description)



class product(models.Model):
    name = models.CharField(max_length=50) 
    Type = models.ForeignKey(product_type, on_delete=models.CASCADE, default='')
    description = models.CharField(max_length=200, null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return '%s (%s)'%(self.name, self.description)
