from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('home_page/', views.HomeView.as_view(), name='home_page'),
]