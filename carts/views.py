import pendulum
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from appointments.models import Appointment
from services.models import Service,ServiceFee
from carts.models import CartItem,AppointmentSchedule
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


def datetime_selector(args):
    map_datename_to_pendulum = {
        'Saturday': pendulum.SATURDAY,
        'Sunday': pendulum.SUNDAY,
        'Monday': pendulum.MONDAY,
        'Tuesday': pendulum.TUESDAY,
        'Wednesday': pendulum.WEDNESDAY,
        'Thursday': pendulum.THURSDAY,
        'Friday': pendulum.FRIDAY,
        }
    date_input = map_datename_to_pendulum.get(args)
    new_date_name = pendulum.now().next(date_input).strftime('%Y-%m-%d')
    return new_date_name

def appointment_fee(service,appointment_type):
    fee = 0
    servicefee = ServiceFee.objects.get(service=service)
    if appointment_type == 'New Appointment':
        fee = servicefee.new_appointment_fee
    elif appointment_type == 'Re-Appointment':
        fee = servicefee.old_appointment_fee
    else:
        fee = servicefee.report_appointment_fee
    return fee
    

class AddToCartView(View):
    login_url = 'users:login'
    def get(self,request):
        if request.user.is_authenticated:
            appointment_type = request.GET.get('appointment_type')
            service_id = request.GET.get('service_id')
            service = Service.objects.get(id=service_id)
            fee = appointment_fee(service,appointment_type)
            next_date = datetime_selector(service.day)
            doctor = service.user
            appointment_schedule,created= AppointmentSchedule.objects.get_or_create(doctor=doctor,appointment_date=next_date)
            try:
                cart_item = CartItem.objects.get(
                    service=service,
                    user=request.user,
                    appointment_schedule = appointment_schedule,
                )
                messages = 'This appointment is already added to your cart!'
            except ObjectDoesNotExist:
                cart_item = CartItem.objects.create(
                    service=service,
                    user=request.user,
                    doctor=doctor,
                    appointment_type=appointment_type,
                    appointment_schedule = appointment_schedule,
                    appointment_fee = fee )
                messages = 'Appointment is added to your cart!'
            
            return JsonResponse({"messages": messages }, status = 200)
        else:
            return JsonResponse({}, status=400)

def total_cart(cart_items):
    total = 0
    for item in cart_items:
        total += item.appointment_fee
    return total

class CartHomeView(LoginRequiredMixin,View):
    login_url = 'users:login'

    template_name = 'carts/cart_home.html'
    def get(self,request):
        cart_items = CartItem.objects.filter(user=request.user,is_active=True)
        total = total_cart(cart_items)
        args = {
            'total':total,
            'cart_items':cart_items
        }
        return render(request,self.template_name,args)

class RemoveCartItem(LoginRequiredMixin,View):
    login_url = 'users:login'
    def get(self,request,pk):
        instance = CartItem.objects.get(id=pk)
        instance.delete()
        return redirect("carts:cart_home")
        

