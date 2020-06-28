from django import forms
import re
from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm
from . import models
from users.models import UserInfo,UserAddress
from addresses.models import Country,Division,City,Area,Address


class UserRegistrationForm(forms.Form):
    UserChoice = (
        ('patient','Patient'),
        ('doctor','Doctor'),
    )

    email = forms.CharField(
        max_length=100,
        required=False,
        widget= forms.TextInput(attrs={'placeholder':'Email'})
    )
    user_type = forms.ChoiceField(
        choices = UserChoice
    )
    

    password1 = forms.CharField(label='Password',max_length=20, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password',max_length=20, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Retype password'}))

    # def check_space(self, username):
    #     for x in username:
    #         if x == ' ':
    #             return True

    #     return False

    def clean(self):
        email       = self.cleaned_data.get('email')
        password1   = self.cleaned_data.get('password1')
        password2   = self.cleaned_data.get('password2')
        if len(email) < 1:
            raise forms.ValidationError('Enter your email address!')
        else:
            email_correction = re.match('^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$', email)
            if not email_correction:
                raise forms.ValidationError('Email format not correct!')
            else:
                email_exist = models.CustomUser.objects.filter(email__iexact=email).exists()
                if email_exist:
                    raise forms.ValidationError('Already sign up with this email! Please change and try again!')
                else:
                    if len(password1) < 8:
                        raise forms.ValidationError("Password is too short!")
                    else:
                        if password1 != password2:
                            raise forms.ValidationError("Password not matched!")
                        


    def deploy(self):
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        user_type = self.cleaned_data.get('user_type')


        user = models.CustomUser(
             email=email,
             user_type=user_type
             )
        user.set_password(password1)
        user.save()
        return user


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', max_length=20, required=False,
    widget= forms.PasswordInput(attrs={'placeholder': 'Old Password'}))

    new_password1 = forms.CharField(label='New Password', max_length=20, required=False,
    widget= forms.PasswordInput(attrs={'placeholder': 'New Password'}))
    
    new_password2 = forms.CharField(label='Confirm Password', max_length=20, required=False,
    widget= forms.PasswordInput(attrs={'placeholder': 'Retype Password'}))

    def clean(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if len(new_password1) < 8:
            raise forms.ValidationError('Password must be minimum 8 digit!')
        else:
            if new_password1 != new_password2 :
                raise forms.ValidationError('Password not matched!')






class EditUserInfoForm(forms.Form):
    GENDER_CHOICES  = (
        ('Male', 'Male'),
        ('Female','Female'),
    )
    mobile = forms.IntegerField(label='Mobile',required=False,
    widget=forms.TextInput(attrs={'placeholder':'01*********'}))

    first_name = forms.CharField(label='First name',
        max_length=50,required=False,
        widget=forms.TextInput(attrs={'placeholder':'First name'}))
    last_name = forms.CharField(label='Last name',
        max_length=50,required=False,
        widget=forms.TextInput(attrs={'placeholder':'Last name'}))    
    gender = forms.ChoiceField(label='Gender',
        choices = GENDER_CHOICES
    )

    religion = forms.CharField(label='Religion',
        max_length=50,required=False,
        widget=forms.TextInput(attrs={'placeholder':'Religion'}))
    dob   = forms.DateField(label="Date Of Birth",
            required=False,
            )
    image = forms.ImageField(label='Image', required=False,)
    
    

    def clean(self):
        first_name   = self.cleaned_data.get('first_name')
        last_name    = self.cleaned_data.get('last_name')
        religion     = self.cleaned_data.get('religion')
        gender       = self.cleaned_data.get('gender')
        image        = self.cleaned_data.get('image')
        mobile       = self.cleaned_data.get('mobile')

        if not first_name:
            raise forms.ValidationError("Give your first name!")
        else:
            if not last_name:
                raise forms.ValidationError("Give your last name!")
            else:
                if not gender:
                    raise forms.ValidationError("Please select your gender!")
        if not mobile:
            raise forms.ValidationError("You must enter your mobile number!")

    def update_info(self,request):
        
        info = UserInfo.objects.get(user=request.user)

        first_name   = self.cleaned_data.get('first_name')
        last_name    = self.cleaned_data.get('last_name')
        religion     = self.cleaned_data.get('religion')
        gender       = self.cleaned_data.get('gender')
        image        = self.cleaned_data.get('image')
        mobile       = self.cleaned_data.get('mobile')
        dob          = self.cleaned_data.get('dob')

        info.first_name = first_name
        info.last_name  = last_name
        info.religion   = religion
        info.gender     = gender
        info.image      = image
        info.mobile     = mobile
        info.dob        = dob
        info.complete   = True


        info.save()




class UserAddressForm(forms.Form):
    area    = forms.CharField(label='Area', max_length=100, required=False,
                    widget=forms.TextInput(attrs={'placeholder':'Lohagara'}))
    address = forms.CharField(label='Address', max_length=100, required=False,
                    widget=forms.TextInput(attrs={'placeholder':'Padua'}))
    def clean(self):
        area = self.cleaned_data.get('area')
        address = self.cleaned_data.get('address')
        if not area or not address:
            raise forms.ValidationError("Please provide your full address!")
    

    def update_user_address(self,request,country_id,division_id,city_id):
        area = self.cleaned_data.get('area')
        address = self.cleaned_data.get('address')


        country_obj = Country.objects.get(id=country_id)
        division_obj = Division.objects.get(id=division_id)
        city_obj = City.objects.get(id=city_id)
        area_obj , created = Area.objects.get_or_create(name=area)
        address_obj , created = Address.objects.get_or_create(name=address)
        
        user_address = UserAddress.objects.get(user=request.user)
        user_address.user = request.user
        user_address.country = country_obj
        user_address.division = division_obj
        user_address.city = city_obj
        user_address.area = area_obj
        user_address.address = address_obj
        
        user_address.save()

