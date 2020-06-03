from django.urls import path
from . import views

app_name = 'medicines'

urlpatterns = [
    path('new_prescription/<slug:appointment_id>/',views.NewPrescriptionView.as_view(),name='new_prescription'),
    path('user/prescription/<slug:user_unique_id>/',views.UserPreviousPrescription.as_view(),name='user_prescription')
]