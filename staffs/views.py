from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from users.models import CustomUser
from doctors.models import DoctorInfo,Speciality
from services.models import Service
from degrees.models import Degree


class DoctorApprovalView(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = "users:login"
    def test_func(self):
        return self.request.user.is_staff
    template_name = 'staffs/doctor_approval.html'
    def get(self,request):
        users = CustomUser.objects.filter(
            user_type = 'doctor',
            is_doctor = False
        )
        services = Service.objects.filter( is_approved = False )
        degrees = Degree.objects.filter( is_approved = False )
        specialitys = Speciality.objects.filter( is_approved = False )
        
        args = {
            'degrees':degrees,
            'services':services,
            'users':users,
            'specialitys':specialitys
        }
        return render(request,self.template_name,args)

class DoctorApproveComplete(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = "users:login"
    def test_func(self):
        return self.request.user.is_staff
    def get(self,request,pk):
        doctor = CustomUser.objects.get(pk=pk)
        doc_info = DoctorInfo.objects.get(user=doctor)
        doc_info.approved_by = self.request.user
        doc_info.is_approved = True
        doc_info.save()
        doctor.is_doctor = True
        doctor.save()
        return redirect("staffs:doctor_approval")

class ServiceApprove(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = "users:login"
    def test_func(self):
        return self.request.user.is_staff
    def get(self,request,pk):
        service = Service.objects.get(pk=pk)
        service.is_approved = True
        service.approved_by = self.request.user
        service.save()
        return redirect("staffs:doctor_approval")


class DegreeApprove(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = "users:login"
    def test_func(self):
        return self.request.user.is_staff
    def get(self,request,pk):
        
        degree = Degree.objects.get(pk=pk)
        degree.is_approved = True
        degree.approved_by = self.request.user
        degree.save()
        
        return redirect("staffs:doctor_approval")

class SpecialityApprove(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = "users:login"
    def test_func(self):
        return self.request.user.is_staff
    def get(self,request,pk):
        
        speciality = Speciality.objects.get(pk=pk)
        speciality.is_approved = True
        speciality.approved_by = self.request.user
        speciality.save()
        
        return redirect("staffs:doctor_approval")

