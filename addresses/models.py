from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name

#State/dividion/Region
class Division(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name
        
#subdivision/Jila/city
class City(models.Model):
    division = models.ForeignKey(Division,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name
#Upojila
class Area(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name
#union/ bla bla
class Address(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name