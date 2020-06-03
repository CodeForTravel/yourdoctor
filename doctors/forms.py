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

 
# class FilterForm(forms.Form):
#     country_choices = [(c.name, c.name) for c in Country.objects.all()]
#     division_choices = [(d.name, d.name) for d in Division.objects.all()]
#     city_choices = [(ct.name, ct.name) for ct in City.objects.all()]
#     # area_choices = [(a.name, a.name) for a in Area.objects.all()]
#     # address_choices = [(ad.name, ad.name) for ad in Address.objects.all()]

#     country = forms.ChoiceField(choices=country_choices,required=False)
#     division = forms.ChoiceField(choices=division_choices,required=False)
#     city = forms.ChoiceField(choices=city_choices,required=False)
#     area = forms.CharField(label='Area',required=False,
#     widget=forms.TextInput(attrs={'placeholder':'Search by upojila name'}))

#     address = forms.CharField(label='Address',required=False,
#     widget=forms.TextInput(attrs={'placeholder':'Search by union name'}))

