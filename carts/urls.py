from django.urls import path
from django.conf.urls import url

from . import views


app_name ='carts'

urlpatterns = [
    path('cart_home',views.CartHomeView.as_view(),name='cart_home'),
    path('add/cart/',views.AddToCartView.as_view(),name='add_to_cart'),
    path('cart/remove/<int:pk>/',views.RemoveCartItem.as_view(),name='remove_item'),
    
 
]