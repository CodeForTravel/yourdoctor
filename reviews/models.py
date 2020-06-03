from django.db import models
from users.models import CustomUser
from django.db.models.signals import pre_save, post_save
from yourdoctor.utils import unique_slug_generator
from appointments.models import Appointment

class Review(models.Model):
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True,related_name='doctor')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True,related_name='user')
    appointment = models.ForeignKey(Appointment,on_delete=models.CASCADE,null=True,blank=True,related_name='appointment')
    comment = models.CharField(max_length=300,null=True,blank=True)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True,unique=True)

    def __str__(self):
        return str(self.user.user_unique_id)


def review_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(review_pre_save_receiver, sender=Review) 