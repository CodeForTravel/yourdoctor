# from django.shortcuts import render
# from django.views import View
# from users.models import CustomUser
# from . import forms

# def is_valid_param(param):
#     print(param)
#     return (param != '') and (param is not None)

# class DoctorFilterView(View):
#     template_name = 'searchs/search_filter.html'
    
#     def get(self,request):

#         #filter form
#         form = forms.FilterForm()

#         #collecting data from web page
#         country = request.GET.get('country')
#         division = request.GET.get('division')
#         city = request.GET.get('city')
#         area = request.GET.get('area')
#         address = request.GET.get('address')
#         # print("Country : " +str(country))
#         # print("Division : " +str(division))
#         # print("City : " +str(city))
#         # print("Area : " +str(area))
#         # print("Address : " +str(address))

        
#         #actual search filtering 
        
#         user_list = CustomUser.objects.filter(user_type='doctor')

#         if is_valid_param(country):
#             user_list = user_list.filter(services__country__name__iexact=country).distinct()
#         if is_valid_param(division):
#             user_list = user_list.filter(services__division__name__iexact=division).distinct()
#         if is_valid_param(city):
#             user_list = user_list.filter(services__city__name__iexact=city).distinct()
#         if is_valid_param(area):
#             user_list = user_list.filter(services__area__name__iexact=area).distinct()
#         if is_valid_param(address):
#             user_list = user_list.filter(services__address__name__iexact=address).distinct()
#             print(user_list)
 
#         args = {
#             'user_list':user_list,
#             'form':form,
#         }
#         return render(request,self.template_name,args)

