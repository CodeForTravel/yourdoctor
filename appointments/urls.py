from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
   
    path('schedule/<int:pk>/', views.AppintmentScheduleView.as_view(), name='appointment_schedule'),
    # path('appointment_confirm/<int:pk>/', views.AppointmentConfirmView.as_view(), name='appointment_confirm'),
    # path('appointment_form/<int:pk>/',views.AppointmentFormView.as_view(),name='appointment_form'),
    path('doctor/appointment/pending/',views.AppointmentPendingView.as_view(),name='pending_appointment'),
    path('mark/appointment/complete/<int:pk>/',views.MarkAppointmentCompleteView.as_view(),name='complete_appointment'),
    # path('completed_appointment/',views.CompletedAppointmentView.as_view(),name='completed_appointment'),
    path('previous_treatment/<slug:appointment_id>/',views.PreviousTreatmentView.as_view(),name='previous_treatment'),
]