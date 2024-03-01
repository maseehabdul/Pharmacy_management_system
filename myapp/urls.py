from django.urls import path
from myapp import views


urlpatterns=[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('login',views.login,name='login_page'),
    path('login/',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout'),
    path('add_medicine',views.add_medicine,name='add_medicine'),
    path('add_customer',views.add_customer,name='add_customer'),
    path('add_dealer',views.add_dealer,name='add_dealer'),
    path('add_purchase',views.add_purchase,name='add_purchase'),       
    path('view_medicine',views.view_medicine,name='view_medicine'),
    path('view_dealer',views.view_dealer,name='view_dealer'),
    path('view_customer',views.view_customer,name='view_customer'),
    path('view_purchase',views.view_purchase,name='view_purchase'),
    path('update_medicine/<str:id>',views.update_medicine, name='update_medicine'),
    path('update_customer/<str:id>',views.update_customer, name='update_customer'),
    path('update_dealer/<str:id>',views.update_dealer, name='update_dealer'),
    path('update_purchase/<str:id>',views.update_purchase, name='update_purchase'),
    path('delete_med/<str:id>',views.delete_med, name='delete_med'),
    path('delete_purchase/<str:id>',views.delete_purchase, name='delete_purchase'),
     path('delete_customer/<str:id>',views.delete_customer, name='delete_customer'),
      path('delete_dealer/<str:id>',views.delete_dealer, name='delete_dealer'),
   
]