from django.urls import path
from myapp import views


urlpatterns=[
    path('',views.index,name='index'),
      path('index',views.index,name='index'),
       path('login',views.login,name='login_page'),
       path('login/',views.login,name='login'),
       path('dashboard',views.dashboard,name='dashboard'),
       path('logout',views.logout,name='logout')
    
]