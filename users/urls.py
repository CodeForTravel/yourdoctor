
from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'users'

urlpatterns = [

#basic 
    path('registration/', views.Registration.as_view(), name='registration'),
    path('user_profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('user/address/',views.UserAddressFormView.as_view(),name='user_address_form'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/home.html'), name="logout"),
    path('edit_user_info/',views.EditUserInfo.as_view(), name = 'edit_user_info'),



#password change 
    path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change-complete/', views.PasswordChangeCompleteView.as_view(), name= 'passwoerd_change_complete'),
#password change complete



#password Reset
    path('password-reset/', views.PasswordResetView.as_view(),name='password_reset'),

    path('password-reset/done/', views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
#password Reset complete   


#API URL
    path('api/division/', views.DivisionAPI.as_view(), name='division_api'),
    path('api/city/', views.CityAPI.as_view(), name='city_api'),
    # path('api/area/', views.AreaAPI.as_view(), name='area_api'),

#Only For Doctor
    path('patient/detail/<int:pk>/',views.UserDetailView.as_view(),name='user_detail')
   ]