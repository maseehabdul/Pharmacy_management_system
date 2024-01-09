from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from requests import request

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(requests):

        return render(requests,'login.html')



    # if requests.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password'];
    #    if request.method == 'POST':
    #       username = request.POST['username']
    #        password = request.POST['password']



  



    # return render(requests,'login.html')


