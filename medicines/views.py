# from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect,Http404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from carts.models import CartItem
from degrees.models import Degree
from medicines.models import Medicine,Test
from users.models import CustomUser
from . import forms

class NewPrescriptionView(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = 'users:login'
    def test_func(self):
        return self.request.user.is_doctor
    template_name = 'medicines/new_prescription.html'
    def get(self,request,appointment_id):
        test_form = forms.TestForm()
        form = forms.AddMedicineForm()
        cart = CartItem.objects.get(appointment_id=appointment_id)
        degrees = Degree.objects.filter(user=cart.doctor)
        
        medicines = Medicine.objects.filter(cart=cart)
        tests = Test.objects.filter(cart=cart)
        args = {
            'tests':tests,
            'test_form':test_form,
            'medicines':medicines,
            'cart':cart,
            'degrees':degrees,
            'form': form
        }
        return render(request,self.template_name,args)
    def post(self,request,appointment_id):
        cart = CartItem.objects.get(appointment_id=appointment_id)
        test_form = forms.TestForm(request.POST or None)
        form = forms.AddMedicineForm(request.POST or None)
        if form.is_valid():
            form.deploy(cart)
            return redirect('medicines:new_prescription', cart.appointment_id)

        if test_form.is_valid():
            test_form.deploy(cart)
            return redirect('medicines:new_prescription', cart.appointment_id)
        variables = {
                'test_form':test_form,
                'form': form
            }
        return render(request, self.template_name,variables)



class UserPreviousPrescription(LoginRequiredMixin,View):
    login_url = 'users:login'

    template_name = 'medicines/user_prev_prescription.html'
    def get(self,request,user_unique_id):
        if request.user.user_unique_id != user_unique_id:
            raise Http404

        user = CustomUser.objects.get(id=request.user.id)
        appointments = CartItem.objects.filter(
            user=user,
            appointment_complete = True
            )

        args = {
            'user':user,
            'appointments':appointments
        }
        return render(request,self.template_name,args)
        
class DeleteMedicine(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = 'users:login'
    def test_func(self):
        return self.request.user.is_doctor
    def get(self,request,pk,appointment_id):
        instance = Medicine.objects.get(id=pk)
        print(str(instance) + " Has Deleted Successfully")
        instance.delete()
        return redirect('medicines:new_prescription', appointment_id)


class DeleteTest(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = 'users:login'
    def test_func(self):
        return self.request.user.is_doctor
    def get(self,request,pk,appointment_id):
        instance = Test.objects.get(id=pk)
        print(str(instance) + " Has Deleted Successfully")
        instance.delete()
        return redirect('medicines:new_prescription', appointment_id)
        