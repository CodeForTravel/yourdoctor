from django import forms
from medicines.models import Medicine,Test

class AddMedicineForm(forms.Form):

    name = forms.CharField(label='Medicine Name',max_length=100,
    widget=forms.TextInput(attrs={'placeholder':'Napa Extra 500mg'}))

    taking_time = forms.CharField(label='Taking Time',max_length=100,
    widget=forms.TextInput(attrs={'placeholder':'1-1-1'}))

    quantity = forms.CharField(label='Quantity',max_length=10,
    widget=forms.TextInput(attrs={'placeholder':'1/2/0.5'}))

    def deploy(self,cart):
        name = self.cleaned_data.get('name')
        taking_time = self.cleaned_data.get('taking_time')
        quantity = self.cleaned_data.get('quantity')

        medicine = Medicine(
            cart = cart,
            name= name,
            taking_time = taking_time,
            quantity = quantity
        )
        medicine.save()

class TestForm(forms.Form):
    
    name = forms.CharField(label='Test Name',max_length=150,
    widget=forms.TextInput(attrs={'placeholder':'RBC'}))

    condition = forms.CharField(label='Test Condition',max_length=200,
    widget=forms.TextInput(attrs={'placeholder':'Morning/Night/Before Eat or ........'}))

    description = forms.CharField(label='Description',max_length=300,
    widget=forms.TextInput(attrs={'placeholder':'Description of test'}))

    def clean(self):
        name = self.cleaned_data.get('name')
        condition = self.cleaned_data.get('condition')
        description = self.cleaned_data.get('description')

        if not name:
            raise forms.ValidationError('Test name cannot empty!')

    def deploy(self,cart):
        name = self.cleaned_data.get('name')
        condition = self.cleaned_data.get('condition')
        description = self.cleaned_data.get('description')

        test = Test(
            cart = cart,
            name = name,
            condition = condition,
            description = description
        )
        test.save()
