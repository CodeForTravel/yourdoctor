from django.db import models
from users.models import CustomUser
from addresses.models import Country,Division,City,Area,Address


class Service(models.Model):
    user        = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    day         = models.CharField(max_length=10,null=True,blank=True)
    start_time  = models.TimeField(null=True,blank=True)
    end_time    = models.TimeField(null=True,blank=True)
    clinic_name = models.CharField(max_length=200,null=True,blank=True)
    active      = models.BooleanField(default=True)
    patient_per_day = models.IntegerField(default=0)

    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,related_name='serviceapproves')
    # Address
    country     = models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    division    = models.ForeignKey(Division,on_delete=models.CASCADE,null=True)
    city        = models.ForeignKey(City,on_delete=models.CASCADE,null=True)
    area        = models.ForeignKey(Area,on_delete=models.CASCADE,null=True)
    address     = models.ForeignKey(Address,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.day


# class ServiceType(models.TextChoices):

#     NEW = 'new', 'New Appointment'
#     RE = 're', 'Re Appointment'
#     REPORT = 'report', 'Report'

class ServiceFee(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE,null=True)
    # service_type =  models.CharField(max_length=100, choices=ServiceType.choices, default=ServiceType.NEW)
    # fee = models.FloatField(default=0, null=True, blank=True)

    new_appointment_fee = models.DecimalField(decimal_places=2, max_digits=20, default='00.00')
    old_appointment_fee = models.DecimalField(decimal_places=2, max_digits=20, default='00.00')
    report_appointment_fee = models.DecimalField(decimal_places=2, max_digits=20, default='00.00')

    def __str__(self):
        return str(self.service.user)


