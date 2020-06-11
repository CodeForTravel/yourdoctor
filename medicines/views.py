# from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect,Http404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from carts.models import CartItem
from degrees.models import Degree
from medicines.models import Medicine
from users.models import CustomUser
from . import forms

class NewPrescriptionView(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = 'users:login'
    def test_func(self):
        return self.request.user.is_doctor
    template_name = 'medicines/new_prescription.html'
    def get(self,request,appointment_id):
        form = forms.AddMedicineForm()
        cart = CartItem.objects.get(appointment_id=appointment_id)
        degrees = Degree.objects.filter(user=cart.doctor)
        
        medicines = Medicine.objects.filter(cart=cart)
        
        args = {
            'medicines':medicines,
            'cart':cart,
            'degrees':degrees,
            'form': form
        }
        return render(request,self.template_name,args)
    def post(self,request,appointment_id):
        cart = CartItem.objects.get(appointment_id=appointment_id)
        form = forms.AddMedicineForm(request.POST or None)
        if form.is_valid():
            form.deploy(cart)
            return redirect('medicines:new_prescription', cart.appointment_id)
        variables = {
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
        
