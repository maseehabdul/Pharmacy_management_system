from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from requests import request
from django.http import HttpResponse



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
           return redirect('/')
       else:
           messages.info(request,'Username or password is invalid!!')
           return redirect("login")
    else:
        return render(request,'login.html')

     



 



  



    # return render(requests,'login.html')


