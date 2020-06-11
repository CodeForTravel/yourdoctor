
from django.shortcuts import render,redirect
# from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views import View
from carts.models import AppointmentSchedule,CartItem
from users.models import CustomUser
from services.models import Service
from degrees.models import Degree


# def schedule_count(s_instance):
#     s_instance.appointment_count += 1;
#     print(s_instance.appointment_count)
#     s_instance.save()

class AppintmentScheduleView(View):
    template_name = 'appointments/appointment_schedule.html'
    def get(self,request,pk):
        
        doctor = CustomUser.objects.get(pk=pk)
        degrees = Degree.objects.all().filter(
            user=doctor,
            is_approved = True
            )
        services = Service.objects.filter(
            user=doctor,
            is_approved = True
            )
        args = {
            'degrees':degrees,
            'doctor':doctor,
            'services':services,
       
        }
        return render(request,self.template_name,args)



class AppointmentPendingView(LoginRequiredMixin,View):
    login_url = 'users:login'
    template_name = 'appointments/appointment_pending.html'
    
    def get(self,request):
        schedules = AppointmentSchedule.objects.filter(doctor=request.user,complete=False)
        items = CartItem.objects.filter(
            doctor=request.user,
            is_active=True,
            appointment_complete = False
            )
        args ={
            'items':items,
            'schedules':schedules,
        }
        return render(request,self.template_name,args)
        


class MarkAppointmentCompleteView(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = 'users:login'
    def test_func(self):
        return self.request.user.is_doctor
    def get(self,request,pk):
        cart = CartItem.objects.get(id=pk)
        cart.appointment_complete = True
        cart.save()
        return redirect('appointments:pending_appointment')

class PreviousTreatmentView(LoginRequiredMixin,View):
    

    template_name = 'appointments/previous_treatment.html'
    def get(self,request,appointment_id):
        cart = CartItem.objects.get(appointment_id=appointment_id)
        appointments = CartItem.objects.filter(user=cart.user,appointment_complete=True)
        
        args = {
            'appointments':appointments
        }
        return render(request,self.template_name,args)

        
class MakeScheduleCompleteView(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = 'users:login'
    def test_func(self):
        return self.request.user.is_doctor
    def get(self,request,pk):
        print(pk)
        ap_schedule = AppointmentSchedule.objects.get(id=pk)
        ap_schedule.complete = True
        ap_schedule.save()
        return redirect("appointments:pending_appointment")