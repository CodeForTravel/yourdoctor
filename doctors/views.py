from django.shortcuts import render,redirect
from django.views import View
from . import forms
from users.models import CustomUser,UserAddress
from doctors.models import DoctorInfo,Speciality,Experience

# from users.models import UserInfo
from services.models import Service
from degrees.models import Degree
from django.contrib.auth.mixins import LoginRequiredMixin
from addresses.models import Country


class DoctorInformationView(LoginRequiredMixin,View):
    template_name = 'doctors/doctor_information_form.html'
    
    def get(self,request):
        if request.user.user_type == 'doctor':
            form = forms.DoctorInformationForm()

            variables = {
                'form':form,
                }
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



# class DoctorListView(View):
#     template_name = 'doctors/doctor_list.html'
#     def get(self,request):
#         user_list = CustomUser.objects.all().filter(user_type__iexact = 'doctor')
        
#         args = {
#             'user_list': user_list,
            
#         }
#         return render(request, self.template_name, args)


class DoctorDetailView(View):
    template_name = 'doctors/doctor_detail.html'
    def get(self,request,pk):
        doctor = CustomUser.objects.get(pk=pk)
        degrees = Degree.objects.all().filter(user=doctor)
        address = UserAddress.objects.get(user=doctor)
        args = {
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
        # print("Country : " +str(country))
        # print("Division : " +str(division))
        # print("City : " +str(city))
        # print("Area : " +str(area))
        # print("Address : " +str(address))

        
        #actual search filtering 
        user_list = CustomUser.objects.filter(user_type='doctor')
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
            print(user_list)
 
        args = {
            'countrys':countrys,
            'user_list':user_list,
            'form':form,
        }
        return render(request,self.template_name,args)

