from django.db import models
from carts.models import CartItem

class Medicine(models.Model):
    cart = models.ForeignKey(CartItem,on_delete=models.CASCADE,null=True,blank=True,related_name='medicines')
    name = models.CharField(max_length=100,null=True,blank=True)
    taking_time = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    cart = models.ForeignKey(CartItem,on_delete=models.CASCADE,null=True,blank=True,related_name='tests')
    name      = models.CharField(max_length=150,null=True,blank=True)
    condition = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.name