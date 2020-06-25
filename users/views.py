from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from . import forms
from django.contrib.auth import views as auth_views
from django.contrib.auth import update_session_auth_hash
from users.models import CustomUser,UserInfo
from django.contrib.auth.mixins import LoginRequiredMixin
from degrees.models import Degree
from services.models import Service
from doctors.models import Speciality
from addresses.models import Country,Division,City,Area,Address
from . import models

## for json data serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
        

class Registration(View):
    template_name = 'users/registration.html'

    def get(self,request):
        form = forms.UserRegistrationForm()
        variables = { 'form':form, }
        return render(request,self.template_name,variables)

    def post(self, request):
        form = forms.UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.deploy()

            #Automatic login after sign-up
            new_user = authenticate(email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],)
            login(request,new_user)

            #a message to user
            messages.success(request, ' Congratulation Sir! Thanks for registration, \
                 Your are successfully logged in!')

            if request.user.user_type == 'doctor':
                return redirect('doctors:doctor_info')
            return redirect('home:home_page')

        variables = { 'form': form, }

        return render(request, self.template_name, variables)

class UserProfileView(LoginRequiredMixin,View):
    login_url = 'users:login'
    template_name = 'users/user_profile.html'
    def get(self,request):
        user = request.user
        degrees = Degree.objects.filter(user=user,is_approved=True)
        services = Service.objects.filter(user=user,is_approved=True)
        user_address = models.UserAddress.objects.get(user=user)
        specialitys  = Speciality.objects.filter(user=user,is_approved=True)
        args = {
            'specialitys':specialitys,
            'user_address':user_address,
            'degrees':degrees,
            'services':services,
            'user':user
        }
        return render(request,self.template_name,args)

class UserDetailView(LoginRequiredMixin,View):
    login_url = 'users:login'
    template_name = 'users/user_detail.html'

    def get(self,request,pk):
        user = CustomUser.objects.get(id=pk)
        args = {
            'user':user
        }
        return render(request,self.template_name,args)

class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = '/users/password-reset/done/'



class PasswordResetDoneView(auth_views.PasswordResetDoneView):
        template_name = 'users/password_reset_done.html'



class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
        template_name = 'users/password_reset_confirm.html'
        success_url = '/users/password-reset-complete/'


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
        template_name = 'users/password_reset_complete.html'



class PasswordChangeView(View):
    template_name = 'users/password_change_form.html'

    def get(self,request):
        form = forms.PasswordChangeForm(user = request.user)
        args = {
            'form':form
        }
        return render(request,self.template_name,args)

    def post(self,request):
        form = forms.PasswordChangeForm(data = request.POST or None, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('users:passwoerd_change_complete')

        args = {
            'form':form
        }
        return render(request,self.template_name,args)




class PasswordChangeCompleteView(View):
    template_name = 'users/password_change_complete.html'

    def get(self,request):
        return render(request,self.template_name)




class EditUserInfo(View):
    template_name = 'users/edit_user_info.html'
    def get(self,request):
        form = forms.EditUserInfoForm()
        variables = {
            'form':form,
            }
        return render(request,self.template_name,variables)
    def post(self, request):
        form = forms.EditUserInfoForm(request.POST or None,request.FILES)
        if form.is_valid():
            form.update_info(request)
            return redirect('users:user_profile')
        variables = {
            'form': form,
            }
        return render(request, self.template_name, variables)

class UserAddressFormView(View):
    template_name = 'users/user_address_form.html'
    def get(self,request):
        form = forms.UserAddressForm()
        countrys = Country.objects.all()
        variables = {
            'form':form,
            'countrys':countrys,
              }
        return render(request,self.template_name,variables)

    def post(self,request):
        form = forms.UserAddressForm(request.POST or None)
        country = request.POST.get('country')
        division = request.POST.get('division')
        city = request.POST.get('city')
        if form.is_valid():
            form.update_user_address(request,country,division,city)
            return redirect('users:user_profile')
        args = {
            'form':form,
                    }
        return render(request,self.template_name,args)


class DivisionAPI(APIView):
    serializer_class = serializers.DivisionSerializer

    def get(self, request):
        if request.GET.get("country_id"):
            country = get_object_or_404(Country, id=request.GET.get("country_id"))
            divisions = Division.objects.filter(country=country)

            data = self.serializer_class(divisions, many=True).data

            return Response({
                "data": data
            }, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class CityAPI(APIView):
    serializer_class = serializers.CitySerializer

    def get(self, request):
        if request.GET.get("division_id"):
            division = get_object_or_404(Division, id=request.GET.get("division_id"))
            cities = City.objects.filter(division=division)

            data = self.serializer_class(cities, many=True).data

            return Response({
                "data": data
            }, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# class AreaAPI(APIView):
#     serializer_class = serializers.AreaSerializer

#     def get(self, request):
#         if request.GET.get("city_id"):
#             city = get_object_or_404(City, id=request.GET.get("city_id"))
#             areas = Area.objects.filter(city=city)

#             data = self.serializer_class(areas, many=True).data

#             return Response({
#                 "data": data
#             }, status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
