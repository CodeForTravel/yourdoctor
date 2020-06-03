from django.urls import path
from django.conf.urls import url

from . import views
from doctors.views import DoctorDetailView

app_name ='doctors'

urlpatterns = [
    path('doctor_info',views.DoctorInformationView.as_view(),name='doctor_info'),
    path('doctor_list',views.DoctorListView.as_view(), name='doctor_list'),
    path('doctor/detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    
]