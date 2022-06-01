from . import views
from django.urls import path 


urlpatterns = [

    # POST reservation and GET
    path('reservation/', views.ReservationAPI.as_view(),name='reservation'),

    
    path('comment/', views.CommentAPI.as_view(),name='comment'),  

    path('managecomment/' ,views.managecomment , name = 'managecomment')

]