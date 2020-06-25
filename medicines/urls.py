from django.urls import path
from . import views

app_name = 'medicines'

urlpatterns = [
    path('new_prescription/<slug:appointment_id>/',views.NewPrescriptionView.as_view(),name='new_prescription'),
    path('user/prescription/<slug:user_unique_id>/',views.UserPreviousPrescription.as_view(),name='user_prescription'),
    path('prescription/delete/medicine/<slug:pk>/<slug:appointment_id>/',views.DeleteMedicine.as_view(),name='delete_medicine'),
    path('prescription/delete/test/<slug:pk>/<slug:appointment_id>/',views.DeleteTest.as_view(),name='delete_test'),
    
]