from django import forms

from . import models 
from users.models import CustomUser
# # from addresses.models import Country,Division,City,Area,Address

class SpecialityForm(forms.Form):
    speciality = forms.CharField(label='Speciality',
        max_length=50,required=False,
        widget=forms.TextInput(attrs={'placeholder':'Speciality'}))

    speciality_details = forms.CharField(label='Speciality Details',
        max_length=400,required=False,
        widget=forms.Textarea(attrs={'placeholder':'Speciality Details'}))

    def clean(self):
        cleaned_data = super(DoctorInformationForm,self).clean()
        speciality = cleaned_data.get('speciality')
        speciality_details = cleaned_data.get('speciality_details')

        if not speciality or speciality_details:
            raise forms.ValidationError("Please all info!")
        
    def deploy(self,request):
        current_working_institution = self.cleaned_data.get('current_working_institution')
        current_working_department = self.cleaned_data.get('current_working_department')
        
        info = models.Speciality(
            user = request.user,
            speciality=speciality,
            speciality_details = speciality_details,

            )
        info.save()


class DoctorInformationForm(forms.Form):
    
    bmdc_number = forms.CharField(label='BMDC Number',
        max_length=30,required=False,
        widget=forms.TextInput(attrs={'placeholder':'BMDC Number'}))

    current_position = forms.CharField(
        label='Current Position',
        max_length=50,required=False,
        widget=forms.TextInput(attrs={'placeholder':'Current Position'}))

    current_working_department = forms.CharField(
        label='Department Name',
        max_length=50,required=False,
        widget=forms.TextInput(attrs={'placeholder':'Medicine'}))

    current_working_institution = forms.CharField(
        label='Current Working Instituation',
        max_length=50,required=False,
        widget=forms.TextInput(attrs={'placeholder':'Chittagong Medical College'}))
    


    def clean(self):
        cleaned_data = super(DoctorInformationForm,self).clean()
        bmdc_number = cleaned_data.get('bmdc_number')
        current_position = cleaned_data.get('current_position')
        speciality = cleaned_data.get('speciality')
        speciality_details = cleaned_data.get('speciality_details')
        
        
        if not bmdc_number :
            raise forms.ValidationError('You must enter the BMDC number!')
        if not current_position:
            raise forms.ValidationError('You must fill up the form!') 

    def deploy(self,request):
        bmdc_number = self.cleaned_data.get('bmdc_number')
        current_position = self.cleaned_data.get('current_position')
        speciality = self.cleaned_data.get('speciality')
        speciality_details = self.cleaned_data.get('speciality_details')
        current_working_institution = self.cleaned_data.get('current_working_institution')
        current_working_department = self.cleaned_data.get('current_working_department')
        
        info = models.DoctorInfo(

            user = request.user,
            bmdc_number=bmdc_number,
            current_position=current_position,
            current_working_institution=current_working_institution,
            current_working_department=current_working_department,
            )
        info.save()

 
class FilterForm(forms.Form):
    
    area = forms.CharField(label='Area',required=False,
    widget=forms.TextInput(attrs={'placeholder':'Search by upojila name'}))

    address = forms.CharField(label='Address',required=False,
    widget=forms.TextInput(attrs={'placeholder':'Search by union name'}))



class SpecialityForm(forms.Form):
    name             = forms.CharField(label='Name Of Speciality',
        max_length=50,required=False,
        widget=forms.TextInput(attrs={'placeholder':'Cardiologists'}))
    
    speciality_details = forms.CharField(label='Details Of Speciality',
        max_length=400,required=False,
        widget=forms.Textarea(attrs={'placeholder':'Explain your speciality within 400 letter'}))

    start_time    = forms.DateTimeField(label='Starting Time Of Speciality',
        widget=forms.TextInput(attrs={'placeholder':'2015-2-12'})
    )
    
    end_time      = forms.DateTimeField(label='Completion Time Of Speciality',
        widget=forms.TextInput(attrs={'placeholder':'2020-4-12'})
    )

    def clean(self):
        name             = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('put your graduation name!')

    def deploy(self,request):
        name             = self.cleaned_data.get('name')
        speciality_details = self.cleaned_data.get('speciality_details')
        start_time    = self.cleaned_data.get('start_time')
        end_time      = self.cleaned_data.get('end_time')


        speciality = models.Speciality(
            user = request.user,
            speciality=name,
            speciality_details = speciality_details,
            start_time = start_time,
            end_time = end_time
        )
        speciality.save()

