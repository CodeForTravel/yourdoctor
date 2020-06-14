from django.shortcuts import render,redirect,Http404
from django.views import View
from . import forms
from services.models import Service
from addresses.models import Country,Division,City,Area,Address
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class ServiceFormView(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = 'users:login'
    def test_func(self):
        return self.request.user.is_doctor

    template_name = 'services/doctor_service_form.html'

    def get(self,request):
        form = forms.DoctorServiceForm()
        countrys = Country.objects.all()
        args = {
            'form':form,
            'countrys':countrys,
              }
        return render(request,self.template_name,args)

    def post(self,request):
        form = forms.DoctorServiceForm(request.POST or None)
        country = request.POST.get('country')
        division = request.POST.get('division')
        city = request.POST.get('city')
        if form.is_valid():
            form.deploy(request,country,division,city)
            return redirect('users:user_profile')
        args = {
            'form':form,
                    }
        return render(request,self.template_name,args)


class ServiceEditView(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = 'users:login'
    def test_func(self):
        return self.request.user.is_doctor
    template_name = 'services/service_edit.html'

    

    def get(self,request,pk):

        DAY_CHOICES  = (
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
    )

        form = forms.EditServiceForm()
        countrys = Country.objects.all()
        service = Service.objects.get(id=pk)
        args = {
            'DAY_CHOICES':DAY_CHOICES,
            'service':service,
            'form':form,
            'countrys':countrys,
        }

        return render(request,self.template_name,args)
    def post(self,request,pk):
        form = forms.EditServiceForm(request.POST or None)
        country = request.POST.get('country')
        division = request.POST.get('division')
        city = request.POST.get('city')
        day = request.POST.get('day')
        print(day)
        if form.is_valid():
            form.update(request,country,division,city,day,pk)
            return redirect('users:user_profile')
        args = {
            'form':form,
                    }
        return render(request,self.template_name,args)