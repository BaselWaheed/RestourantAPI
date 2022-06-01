
from django.urls import path 
from . import views 

urlpatterns = [

    path('cart/', views.CartPostGetVIEW.as_view(), name = 'cart'),

    path('checkout/', views.CheckoutAPI.as_view(), name = 'checkout'),

    path('orderhistory/',views.MyOrderAPI.as_view(), name = "orderhistory"),

    path('orderdetails/',views.OrderDetailsAPI.as_view(), name= "orderdetails"),

    
]