
from django.shortcuts import render,redirect
# from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# from . import forms
# from . import models
from carts.models import AppointmentSchedule,CartItem
from users.models import CustomUser
from services.models import Service

# from medicines.models import Medicine
from degrees.models import Degree
# from .forms import datetime_selector

# def schedule_count(s_instance):
#     s_instance.appointment_count += 1;
#     print(s_instance.appointment_count)
#     s_instance.save()

class AppintmentScheduleView(View):
    template_name = 'appointments/appointment_schedule.html'
    def get(self,request,pk):
        
        doctor = CustomUser.objects.get(pk=pk)
        degrees = Degree.objects.all().filter(user=doctor)
        services = Service.objects.filter(user=doctor)
        args = {
            'degrees':degrees,
            'doctor':doctor,
            'services':services,
       
        }
        return render(request,self.template_name,args)

# class AppointmentConfirmView(LoginRequiredMixin,View):
#     login_url = 'users:login'
#     def get(self,request,pk):
#         user = request.user
#         if user.userinfo.complete:
#             #Query Data
#             service = Service.objects.get(pk=pk)
#             next_date = datetime_selector(service.day)
#             service = Service.objects.get(pk=pk)
#             doctor = CustomUser.objects.get(services__pk=pk)

#             try:
#                 appointment_schedule = AppointmentSchedule.objects.get(doctor=doctor,appointment_date__iexact=next_date)
#             except AppointmentSchedule.DoesNotExist:
#                 appointment_schedule = AppointmentSchedule.objects.create(doctor=doctor,appointment_date=next_date)

#             if appointment_schedule.appointment_count >10:
#                 messages.warning(request, 'Appoinment limit is full.! please try another date or doctor') 
#                 return redirect('doctors:doctor_list')
            
            
#             patienr_user = request.user
#             first_name = patienr_user.userinfo.first_name 
#             last_name =  patienr_user.userinfo.last_name
#             new_appointment = Appointment(
#                 doctor=doctor,
#                 patient=patienr_user,
#                 appointment_schedule=appointment_schedule,
#                 mobile=patienr_user.userinfo.mobile,
#                 first_name = first_name,
#                 last_name = last_name
#             )
#             schedule_count(appointment_schedule)
#             new_appointment.save()
#             messages.success(request, 'You just add an appointment to your \
#              wish list! Please Check-out quickly to confirm your appointment!!!')
#             return redirect('doctors:doctor_list')
#         return redirect('appointments:appointment_form', pk=pk)


# class AppointmentFormView(LoginRequiredMixin,View):
#     login_url = 'users:login'
#     template_name = 'appointments/appointment_form.html'

#     def get(self,request,pk):
#         form = forms.AppointmentForm()
#         args = { 'form':form, }
#         return render(request,self.template_name,args)

#     def post(self,request,pk):
#         form = forms.AppointmentForm(request.POST or None)
#         if form.is_valid():
#             form.deploy(request,pk)
#             return redirect('doctors:doctor_list')
#         variable = {
#                 'form': form,
#             }
#         return render(request, self.template_name,variable)


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
        

# class CompletedAppointmentView(LoginRequiredMixin,View):
#     login_url = 'users:login'
#     template_name = 'appointments/appointment_completed.html'

#     def get(self,request):
#         user = request.user
#         appointments = Appointment.objects.filter(doctor=user,appointment_complete=True)
#         args = {
#             'user':user,
#             'appointments':appointments
#         }
#         return render(request,self.template_name,args)

class MarkAppointmentCompleteView(LoginRequiredMixin,View):
    login_url = 'users:login'
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

        
        