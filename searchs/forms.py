# from django import forms
# from addresses.models import Country,Division,City,Area,Address



# class FilterForm(forms.Form):
#     country_choices = [(c.name, c.name) for c in Country.objects.all()]
#     division_choices = [(d.name, d.name) for d in Division.objects.all()]
#     city_choices = [(ct.name, ct.name) for ct in City.objects.all()]
#     # area_choices = [(a.name, a.name) for a in Area.objects.all()]
#     # address_choices = [(ad.name, ad.name) for ad in Address.objects.all()]

#     country = forms.ChoiceField(choices=country_choices)
#     division = forms.ChoiceField(choices=division_choices)
#     city = forms.ChoiceField(choices=city_choices)
#     area = forms.CharField(label='Area',required=False,
#     widget=forms.TextInput(attrs={'placeholder':'Search by upojila name'}))

#     address = forms.CharField(label='Address',required=False,
#     widget=forms.TextInput(attrs={'placeholder':'Search by union name'}))


    