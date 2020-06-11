from django.db import models
from carts.models import CartItem

class Medicine(models.Model):
    cart = models.ForeignKey(CartItem,on_delete=models.CASCADE,null=True,blank=True,related_name='medicines')
    name = models.CharField(max_length=100,null=True,blank=True)
    taking_time = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.name