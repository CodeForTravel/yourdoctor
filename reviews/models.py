from django.db import models
from django.db.models import Avg
from users.models import CustomUser
from django.db.models.signals import pre_save, post_save
from carts.models import CartItem


class ReviewManager(models.Manager):
    def avg_rating(self,doctor):
        avg_rating = 0
        avg =  self.filter(doctor=doctor).aggregate(Avg('rating'))
        if avg:
            avg_rating = avg_rating  = avg['rating__avg']
        return avg_rating



class Review(models.Model):
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True,related_name='doctor')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True,related_name='user')
    cart = models.ForeignKey(CartItem,on_delete=models.SET_NULL,null=True,blank=True)
    comment = models.CharField(max_length=300,null=True,blank=True)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ReviewManager()

    def __str__(self):
        return str(self.user.user_unique_id)


