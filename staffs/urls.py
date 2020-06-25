from django.urls import path
from . import views

app_name = 'staffs'

urlpatterns = [
    path('apporove/doctor/',views.DoctorApprovalView.as_view(), name='doctor_approval'),
    path('apporove/doctor/complete/<int:pk>/',views.DoctorApproveComplete.as_view(), name='approval_complete'),
    path('apporove/doctor/service/<int:pk>/',views.ServiceApprove.as_view(), name='service_approval'),
    path('apporove/doctor/degree/<int:pk>/',views.DegreeApprove.as_view(), name='degree_approval'),
    path('apporove/doctor/speciality/<int:pk>/',views.SpecialityApprove.as_view(), name='speciality_approval'),
    
]