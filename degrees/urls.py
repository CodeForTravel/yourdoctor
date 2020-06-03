from django.urls import path
from . import views

app_name = 'degrees'

urlpatterns = [

    path('degree_form/', views.DegreeFormView.as_view(), name='degree_form'),
   
]