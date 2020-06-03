from django.db import models
from users.models import CustomUser

class Degree(models.Model):
    user             = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name             = models.CharField(max_length=50,null=True,blank=True)
    institution_name = models.CharField(max_length=200,null=True,blank=True)
    starting_time    = models.DateTimeField(null=True,blank=True)
    ending_time      = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.user.email