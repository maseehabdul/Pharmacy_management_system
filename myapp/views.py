from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from .models import medicine



# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username=username,password=password)
       
       if user is not None:
           auth.login(request,user)
           return redirect('dashboard')
       else:
           messages.info(request,'Username or password is invalid!!')
           return redirect("login")
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')
        

def dashboard(request):
    if request.user.is_authenticated:
       return render(request,'dashboard.html')
    else:
        return redirect(login)
    
def add_medicine(request):
    return render(request,'add_medicine.html')

def view_medicine(request):
    if request.user.is_authenticated:
        medicines = medicine.objects.all()
        return render(request,'view_medicine.html',{"medicine": medicines})
    else:
        return redirect('login')

   
        
    


    
     



 



  



    # return render(requests,'login.html')


