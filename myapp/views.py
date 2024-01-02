from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(requests):
    return render(requests,'login.html')