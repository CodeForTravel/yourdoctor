from django.urls import path
from . import views


app_name ='reviews'

urlpatterns = [
    path('review_form',views.ReviewFormView.as_view(),name='review_form'),
]