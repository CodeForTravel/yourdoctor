from django import forms
from services.models import Service,ServiceFee
from addresses.models import Country,Division,City,Area,Address


class DoctorServiceForm(forms.Form):
    DAY_CHOICES  = (
        ('Saturday','Saturday'),
        ('Sunday','Sunday'),
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
    )
    
    day         = forms.ChoiceField(label='Day' , choices = DAY_CHOICES)

    start_time  = forms.TimeField(label='Service Starting Time'
                    # widget=forms.TimeField(attrs={'placeholder':'12.30'})
                    )

    end_time    = forms.TimeField(label='Service Ending Time'
                    # widget=forms.TimeField(attrs={'placeholder':'12.30'})
                     )
    clinic_name = forms.CharField(label='Clinic Name',max_length=200, required=False,
                    widget=forms.TextInput(attrs={'placeholder':'National Hospital'}))

    new_appointment_fee = forms.DecimalField(label="New appointment fee",decimal_places=2, max_digits=20)
    old_appointment_fee = forms.DecimalField(label="Old appointment fee",decimal_places=2, max_digits=20)
    report_appointment_fee = forms.DecimalField(label="Report showing appointment fee",decimal_places=2, max_digits=20)
    

    area    = forms.CharField(label='Area', max_length=100, required=False,
                    widget=forms.TextInput(attrs={'placeholder':'Lohagara'}))
    address = forms.CharField(label='Address', max_length=100, required=False,
                    widget=forms.TextInput(attrs={'placeholder':'Padua'}))


    def clean(self):
        day = self.cleaned_data.get('day')
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        clinic_name = self.cleaned_data.get('clinic_name')
        new_appointment_fee = self.cleaned_data.get('new_appointment_fee')
        old_appointment_fee = self.cleaned_data.get('old_appointment_fee')
        report_appointment_fee = self.cleaned_data.get('report_appointment_fee')

        area = self.cleaned_data.get('area')
        address = self.cleaned_data.get('address')

        if not day:
            raise forms.ValidationError("Select the service day!")
        else:
            if not start_time or not end_time:
                raise forms.ValidationError("You must enter service time!")
            else:
                if not clinic_name:
                    raise forms.ValidationError("You must give the clinic name!")
                else:
                    if not new_appointment_fee:
                        raise forms.ValidationError("Please enter your desired fee!")

        if not area or not address:
            raise forms.ValidationError('Please enter the full address!')

    def deploy(self,request,country_id,division_id,city_id):

        day         = self.cleaned_data.get('day')
        start_time  = self.cleaned_data.get('start_time')
        end_time    = self.cleaned_data.get('end_time')
        clinic_name = self.cleaned_data.get('clinic_name')
        new_appointment_fee = self.cleaned_data.get('new_appointment_fee')
        old_appointment_fee = self.cleaned_data.get('old_appointment_fee')
        report_appointment_fee = self.cleaned_data.get('report_appointment_fee')

        area = self.cleaned_data.get('area')
        address = self.cleaned_data.get('address')

        country_obj = Country.objects.get(id=country_id)
        division_obj = Division.objects.get(id=division_id)
        city_obj = City.objects.get(id=city_id)
        area_obj , created = Area.objects.get_or_create(name=area)
        address_obj , created = Address.objects.get_or_create(name=address)

        

        service = Service(
            user       = request.user,
            day        = day,
            start_time = start_time,
            end_time   = end_time,
            clinic_name = clinic_name,

            country    = country_obj,
            division   = division_obj,
            city       = city_obj,
            area       = area_obj,
            address    = address_obj

        )
        service.save()

        
        new_service_fee = ServiceFee(
            service = service,
            new_appointment_fee=new_appointment_fee,
            old_appointment_fee=old_appointment_fee,
            report_appointment_fee=report_appointment_fee,
            )
        new_service_fee.save()


class EditServiceForm(forms.Form):
    start_time  = forms.TimeField(label='Service Starting Time'
                    # widget=forms.TimeField(attrs={'placeholder':'12.30'})
                    )

    end_time    = forms.TimeField(label='Service Ending Time'
                    # widget=forms.TimeField(attrs={'placeholder':'12.30'})
                     )
    clinic_name = forms.CharField(label='Clinic Name',max_length=200, required=False,
                    widget=forms.TextInput(attrs={'placeholder':'National Hospital'}))

    new_appointment_fee = forms.DecimalField(label="New appointment fee",decimal_places=2, max_digits=20)
    old_appointment_fee = forms.DecimalField(label="Old appointment fee",decimal_places=2, max_digits=20)
    report_appointment_fee = forms.DecimalField(label="Report showing appointment fee",decimal_places=2, max_digits=20)
    

    area    = forms.CharField(label='Area', max_length=100, required=False,
                    widget=forms.TextInput(attrs={'placeholder':'Lohagara'}))
    address = forms.CharField(label='Address', max_length=100, required=False,
                    widget=forms.TextInput(attrs={'placeholder':'Padua'}))


    def clean(self):
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        clinic_name = self.cleaned_data.get('clinic_name')
        new_appointment_fee = self.cleaned_data.get('new_appointment_fee')
        old_appointment_fee = self.cleaned_data.get('old_appointment_fee')
        report_appointment_fee = self.cleaned_data.get('report_appointment_fee')

        area = self.cleaned_data.get('area')
        address = self.cleaned_data.get('address')

        

        if not start_time or not end_time:
            raise forms.ValidationError("You must enter service time!")
        else:
            if not clinic_name:
                raise forms.ValidationError("You must give the clinic name!")
            else:
                if not new_appointment_fee:
                    raise forms.ValidationError("Please enter your desired fee!")

        if not area or not address:
            raise forms.ValidationError('Please enter the full address!')

    def update(self,request,country_id,division_id,city_id,day,pk):
        start_time  = self.cleaned_data.get('start_time')
        end_time    = self.cleaned_data.get('end_time')
        clinic_name = self.cleaned_data.get('clinic_name')
        new_appointment_fee = self.cleaned_data.get('new_appointment_fee')
        old_appointment_fee = self.cleaned_data.get('old_appointment_fee')
        report_appointment_fee = self.cleaned_data.get('report_appointment_fee')

        area = self.cleaned_data.get('area')
        address = self.cleaned_data.get('address')

        country_obj = Country.objects.get(id=country_id)
        division_obj = Division.objects.get(id=division_id)
        city_obj = City.objects.get(id=city_id)
        area_obj , created = Area.objects.get_or_create(name=area)
        address_obj , created = Address.objects.get_or_create(name=address)

        
        service = Service.objects.get(id=pk)
        
        
        service.user       = request.user
        service.day        = day
        service.start_time = start_time
        service.end_time   = end_time
        service.clinic_name = clinic_name

        service.country    = country_obj
        service.division   = division_obj
        service.city       = city_obj
        service.area       = area_obj
        service.address    = address_obj
        service.is_approved = False

        

        fee = ServiceFee.objects.get(service = service)
        
        
        fee.new_appointment_fee=new_appointment_fee
        fee.old_appointment_fee=old_appointment_fee
        fee.report_appointment_fee=report_appointment_fee
            

        service.save()
        fee.save()
        