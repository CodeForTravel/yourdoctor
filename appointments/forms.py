import pendulum
from django import forms
from . import models 
from users.models import CustomUser,UserInfo
from services.models import Service
from appointments.models import Appointment,AppointmentSchedule


def datetime_selector(args):
    print(args)
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



class AppointmentForm(forms.Form):
    mobile = forms.CharField(label='Mobile Number',max_length=20,required=False,
        widget=forms.TextInput(attrs={'placeholder':'018*******'}))

    first_name = forms.CharField(label='First Name',max_length=100,required=False,
        widget=forms.TextInput(attrs={'placeholder':'Mohammad '}))
    
    last_name = forms.CharField(label='Last Name',max_length=100,required=False,
        widget=forms.TextInput(attrs={'placeholder':'Abul'}))

    def clean(self):
        mobile = self.cleaned_data.get('mobile')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if not mobile:
            raise forms.ValidationError('Dare user, you have  to provide your mobile \
         number! That will help us to emergency contact ')
        else:
            if not first_name or not last_name:
                raise forms.ValidationError('Please sir, provide your full name!')

    def deploy(self,request,pk):
        #form_data
        mobile = self.cleaned_data.get('mobile')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        #Query Data
        next_date = datetime_selector(service.day)
        service = Service.objects.get(pk=pk)
        doctor = CustomUser.objects.get(services__pk=pk)

        try:
            appointment_schedule = AppointmentSchedule.objects.get(doctor=doctor,appointment_date__iexact=next_date)
        except AppointmentSchedule.DoesNotExist:
            appointment_schedule = AppointmentSchedule.objects.create(doctor=doctor,appointment_date=next_date)

        patienr_user = request.user
        new_appointment = Appointment(
            doctor=doctor,
            patient=patienr_user,
            appointment_schedule=appointment_schedule,
            mobile=mobile,
            first_name=first_name,
            last_name=last_name,
        )
        new_appointment.save()
        
        #save data to UserInfo table
        user_info = UserInfo.objects.get(user=patienr_user)
        user_info.first_name = first_name
        user_info.last_name = last_name
        user_info.complete = True
        user_info.save()
