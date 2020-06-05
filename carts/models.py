from django.db import models
from yourdoctor.utils import order_id
from yourdoctor.utils import unique_appointment_id_generator
import pendulum
from django.db.models.signals import pre_save
from users.models import CustomUser
from services.models import Service


class AppointmentSchedule(models.Model):
    doctor = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    appointment_date = models.DateField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    appointment_count = models.IntegerField(default=0)

    @property
    def day(self):
        strrrr = str(self.appointment_date)
        dt = pendulum.parse(strrrr, strict=False)
        return dt.format(' DD-MM-YYYY : dddd ')

    def __str__(self):
        return str(self.appointment_date)

    def appointment_count_func(self):
        self.appointment_count += 1


class CartItem(models.Model):
    appointment_id = models.CharField(max_length=50,blank=True,null=True)
    service = models.ForeignKey(Service,on_delete=models.SET_NULL,null=True,related_name='services')
    user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,related_name='users')
    doctor = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,related_name="doctors")
    appointment_type = models.CharField(max_length=100,null=True,blank=True)
    appointment_schedule = models.ForeignKey(AppointmentSchedule,on_delete=models.SET_NULL,null=True,related_name='appointment_schedules')
    appointment_fee = models.DecimalField(decimal_places=2, max_digits=10, default='00.00')
    appointment_complete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.service.day

def per_save_create_appointment_id(sender,instance,*args,**kwargs): 
    if not instance.appointment_id:
        instance.appointment_id = unique_appointment_id_generator(instance)
pre_save.connect(per_save_create_appointment_id,sender=CartItem)



class PaymentStatusChoice(models.TextChoices):
    PENDING = 'pending', 'Pending'
    COMPLETE = 'complete', 'Complete'
    failed = 'failed', 'Failed'

class ProviderChoice(models.TextChoices):
    BKASH = 'Bkash', 'Bkash'
    NAGAD = 'Nagad', 'Nagad'
    ROCKET = 'Rocket', 'Rocket'

class Payment(models.Model):

    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name='orders')
    provider = models.CharField(max_length=100, choices=ProviderChoice.choices, default=ProviderChoice.BKASH)
    transaction_id = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, choices=PaymentStatusChoice.choices, default=PaymentStatusChoice.PENDING)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class OrderStatusChoice(models.TextChoices):
    PENDING_PAYMENT = 'pending_payment', 'Pending Payment'
    PROCESSING = 'processing', 'Processing'
    REFUND_INITIATED = 'refund_initiated', 'Refund Initiated'
    REFUNDED = 'refunded', 'Refunded'

class Order(models.Model):
    order_id = models.CharField(max_length=20,unique=True, default=order_id())
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    carts = models.ManyToManyField(CartItem)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,null=True, related_name="payments")
    # confirmed_by = models.ForeignKey(
    #     CustomUser, 
    #     on_delete=models.SET_NULL, 
    #     null=True, 
    #     blank=True, 
    #     related_name='stuff'
    # )
    status = models.CharField(max_length=100, choices=OrderStatusChoice.choices, default=OrderStatusChoice.PENDING_PAYMENT)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return round(sum(o.appointment_fee for o in self.carts.all()), 2) if self.carts.all() else 0


    def __str__(self):
        return self.order_id

