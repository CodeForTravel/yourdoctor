from django.shortcuts import render,redirect
from django.views import View
from . import forms
from reviews.forms import ReviewForm
from users.models import CustomUser,UserAddress
from doctors.models import DoctorInfo,Speciality,Experience

# from users.models import UserInfo
from carts.models import CartItem
from services.models import Service
from degrees.models import Degree
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from addresses.models import Country


class DoctorInformationView(LoginRequiredMixin,View):
    login_url = 'users:login'
    template_name = 'doctors/doctor_information_form.html'
    
    def get(self,request):
        if request.user.user_type == 'doctor':
            form = forms.DoctorInformationForm()
            variables = {
                'form':form,
                }
        else:
            return redirect('users:user_profile')
        return render(request,self.template_name,variables)

    def post(self, request):
        form = forms.DoctorInformationForm(request.POST or None)
        if form.is_valid():
            form.deploy(request)
            return redirect('home:home_page')
        variables = {
                'form': form,
            }
        return render(request, self.template_name, variables)



class DoctorDetailView(View):
    template_name = 'doctors/doctor_detail.html'
    def get(self,request,pk):
        last_appointment = None
        form = ReviewForm()
        doctor = CustomUser.objects.get(pk=pk)
        degrees = Degree.objects.all().filter(user=doctor,is_approved=True)
        address = UserAddress.objects.get(user=doctor)
        specialitys = Speciality.objects.filter(user=doctor,is_approved=True)
        cartitems = CartItem.objects.filter(
                                            user = request.user,
                                            is_reviewed =False,
                                            appointment_complete=True,
                                            )
        if cartitems:
            last_appointment = cartitems.last()
        args = {
            'last_appointment':last_appointment,
            'cartitems':cartitems,
            'form':form,
            'specialitys':specialitys,
            'address':address,
            'doctor':doctor,
            'degrees':degrees
        }
        return render(request,self.template_name,args)


def is_valid_param(param):
    return (param != '') and (param is not None)

class DoctorListView(View):
    template_name = 'doctors/doctor_list.html'
    
    def get(self,request):
        form = forms.FilterForm()
        countrys = Country.objects.all()
        #collecting data from web page
        country = request.GET.get('country')
        division = request.GET.get('division')
        city = request.GET.get('city')
        area = request.GET.get('area')
        address = request.GET.get('address')

        #actual search filtering 
        user_list = CustomUser.objects.filter(user_type='doctor',is_doctor=True)
        if is_valid_param(country):
            user_list = user_list.filter(service__country__id=country).distinct()
        if is_valid_param(division):
            user_list = user_list.filter(service__division__id=division).distinct()
        if is_valid_param(city):
            user_list = user_list.filter(service__city__id=city).distinct()
        if is_valid_param(area):
            user_list = user_list.filter(service__area__name__iexact=area).distinct()
        if is_valid_param(address):
            user_list = user_list.filter(service__address__name__iexact=address).distinct()


        degrees = Degree.objects.filter(is_approved = True)
        specialitys = Speciality.objects.filter(is_approved = True)
 


        args = {
            'specialitys':specialitys,
            'degrees':degrees,
            'countrys':countrys,
            'user_list':user_list,
            'form':form,
        }
        return render(request,self.template_name,args)


class SpecialityForm(LoginRequiredMixin,View):
    login_url = 'users:login'
    
    template_name = 'doctors/speciality_form.html'
    def get(self,request):
        form = forms.SpecialityForm()
        args = {
            'form':form,
        }
        return render(request,self.template_name,args)
    def post(self, request):
        form = forms.SpecialityForm(request.POST or None)
        if form.is_valid():
            form.deploy(request)
            return redirect('users:user_profile')
        variables = {
            'form': form,
            }
        return render(request, self.template_name, variables)
