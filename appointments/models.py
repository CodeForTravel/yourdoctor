from django.db import models
from users.models import CustomUser
from services.models import Service
from yourdoctor.utils import unique_appointment_id_generator
from django.db.models.signals import pre_save
from carts.models import CartItem






class Appointment(models.Model):
    cart = models.ForeignKey(CartItem,on_delete=models.SET_NULL,null=True,related_name='carts')
    doctor = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='appointed_doctor',null=True)
    patient = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='appointed_patient',null=True)
    appointment_id = models.CharField(max_length=50,blank=True,null=True)
    appointment_complete = models.BooleanField(default=False)
    #payment = models.ForeignKey("Payment", on_delete=models.SET_NULL, null=True)
    #payment_complete     = models.BooleanField(default=False)
    
    def __str__(self):
        return self.patient.email










def per_save_create_appointment_id(sender,instance,*args,**kwargs): 
    if not instance.appointment_id:
        instance.appointment_id = unique_appointment_id_generator(instance)

pre_save.connect(per_save_create_appointment_id,sender=Appointment)