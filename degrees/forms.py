from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from degrees.models import Degree
# from .widgets import BootstrapDateTimePickerInput


class DegreeForm(forms.Form):
    name             = forms.CharField(label='Name Of Degree',
        max_length=50,required=False,
        widget=forms.TextInput(attrs={'placeholder':'MBBS/BDS/FCPS/MD/MS/MRCP/FRCP...'}))
    
    subject = forms.CharField(label='Subject of Degree',
        max_length=50,required=False,
        widget=forms.TextInput(attrs={'placeholder':'Health(If possible)'}))

    institution_name = forms.CharField(label='Name Of Institution',
        max_length=200,required=False,
        widget=forms.TextInput(attrs={'placeholder':'Chittagong Medical College(CMC)'}))

    starting_time    = forms.DateTimeField(label='Starting Time Of Degree',
        widget=forms.TextInput(attrs={'placeholder':'2020-2-12'})
    )
    
    ending_time      = forms.DateTimeField(label='Completion Time Of Degree',
        widget=forms.TextInput(attrs={'placeholder':'2020-4-12'})
    )

    def clean(self):
        name             = self.cleaned_data.get('name')
        institution_name = self.cleaned_data.get('institution_name')
        starting_time    = self.cleaned_data.get('starting_time')
        ending_time      = self.cleaned_data.get('ending_time')

        if not name:
            raise forms.ValidationError('put your graduation name!')
        else:
            if not institution_name:
                raise forms.ValidationError('put your institution name!')

    def deploy(self,request):
        name             = self.cleaned_data.get('name')
        institution_name = self.cleaned_data.get('institution_name')
        starting_time    = self.cleaned_data.get('starting_time')
        ending_time      = self.cleaned_data.get('ending_time')
        subject          = self.cleaned_data.get('subject')


        degree = Degree(
            subject=subject,
            user = request.user,
            name=name,
            institution_name = institution_name,
            starting_time = starting_time,
            ending_time = ending_time
        )
        degree.save()

