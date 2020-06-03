from django import forms
from medicines.models import Medicine

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
