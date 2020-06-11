from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
   
    path('schedule/<int:pk>/', views.AppintmentScheduleView.as_view(), name='appointment_schedule'),
    path('schedule/make/complete/<int:pk>/', views.MakeScheduleCompleteView.as_view(), name='make_schedule_complete'),
    path('doctor/appointment/pending/',views.AppointmentPendingView.as_view(),name='pending_appointment'),
    path('mark/appointment/complete/<int:pk>/',views.MarkAppointmentCompleteView.as_view(),name='complete_appointment'),
    path('previous_treatment/<slug:appointment_id>/',views.PreviousTreatmentView.as_view(),name='previous_treatment'),
]