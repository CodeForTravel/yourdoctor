from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save,pre_save
from django.urls import reverse
from addresses.models import Country,Division,City,Area,Address

from yourdoctor.utils import unique_user_id_generator




class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have a email address! ')

        email = self.normalize_email(email)
        user = self.model(email=email)

        user.set_password(password)
        user.save(using = self._db)

        return user
    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    UserChoice = (
        ('patient', 'Patient'),
        ('doctor','Doctor'),
    )

    email = models.EmailField(max_length=255, unique=True)
    user_type = models.CharField(max_length=10,
    choices = UserChoice
    )
    user_unique_id  = models.CharField(max_length=20, blank=True,null=True)
    join_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    def __str__(self):
        return self.email


class UserInfo(models.Model):
#users personal information
    GENDER_CHOICES  = (
        ('Male', 'Male'),
        ('Female','Female'),
    )
    mobile    = models.IntegerField(default=0,null=True,blank=True)
    user         = models.OneToOneField(CustomUser, on_delete=models.CASCADE )
    first_name   = models.CharField(max_length=50,null=True,blank=True)
    last_name    = models.CharField(max_length=50,null=True,blank=True)
    religion     = models.CharField(max_length=50,null=True,blank=True)
    gender       = models.CharField(max_length=10,choices=GENDER_CHOICES)
    image        = models.ImageField(upload_to='user_image/',blank=True,null=True)
    complete     = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

class UserAddress(models.Model):
    user        = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    country     = models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    division    = models.ForeignKey(Division,on_delete=models.CASCADE,null=True,blank=True)
    city        = models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True)
    area        = models.ForeignKey(Area,on_delete=models.CASCADE,null=True,blank=True)
    address     = models.ForeignKey(Address,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.user.email


def create_user_unique_id(sender, instance, *args, **kwargs): 
    if not instance.user_unique_id:
        instance.user_unique_id = unique_user_id_generator(instance)    
pre_save.connect(create_user_unique_id,sender=CustomUser)

def create_userinfo(sender,**kwargs ):
    if kwargs['created']:
        userinfo =UserInfo.objects.create(user=kwargs['instance'])
post_save.connect(create_userinfo,sender=CustomUser)

def create_useraddress(sender,**kwargs ):
    if kwargs['created']:
        useraddress =UserAddress.objects.create(user=kwargs['instance'])
post_save.connect(create_useraddress,sender=CustomUser)

