"""yourdoctor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import HomeView


'''______ for image file_____'''
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(),name='home'),
    path('users/', include('users.urls', namespace='users')),
    path('doctors/', include('doctors.urls', namespace='doctors')),
    path('home/', include('home.urls', namespace='home')),
    path('degrees/', include('degrees.urls', namespace='degrees')),
    path('appointments/', include('appointments.urls', namespace='appointments')),
    path('services/', include('services.urls', namespace='services')),
    path('medicines/', include('medicines.urls', namespace='medicines')),
    path('searchs/', include('searchs.urls', namespace='searchs')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('carts/', include('carts.urls', namespace='carts')),
    path('staffs/', include('staffs.urls', namespace='staffs')),

    
    #path('', include('django.contrib.auth.urls')),  appointment
]

'''______for view the uploaded images locally.'''
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)