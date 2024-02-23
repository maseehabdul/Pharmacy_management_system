from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from myapp.form import addmedicine
from .models import medicine,dealer,customer,purchase





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
    
    # add a items function
    
def add_medicine(request):
    addmedicines = addmedicine()
    if request.method == 'POST':
        addmedicines = addmedicine(request.POST)
        if addmedicines.is_valid():
            addmedicines.save()
            return redirect('add_medicine')
    return render(request,'addvalues/add_medicine.html',{'addmedicines':addmedicines})



# update values 
def update_medicine(request, id):
    medicines = medicine.objects.all().filter(id=id)
    # addmedicines = addmedicine(instance=medicine)
    return render(request,'updatefiles/update_medicine.html', {'medicines':medicines,})


    



#view a items functions

def view_medicine(request):
    if request.user.is_authenticated:
        medicines = medicine.objects.all()
        return render(request,'viewfiles/view_medicine.html',{"medicine": medicines})
    else:
        return redirect('login')
    
def view_dealer(request):
    if request.user.is_authenticated:
        dealers = dealer.objects.all()
        return render(request,'viewfiles/view_dealer.html',{"dealer": dealers})
    else:
        return redirect('login')
def view_customer(request):
    if request.user.is_authenticated:
        customers = customer.objects.all()
        return render(request,'viewfiles/view_customer.html',{"customer": customers})
    else:
        return redirect('login')
    
def view_purchase(request):
    if request.user.is_authenticated:
        purchases = purchase.objects.all()
        return render(request,'viewfiles/view_purchase.html',{"purchases": purchases})
    else:
        return redirect('login')
    




   
    
    


    
     



 



  



    # return render(requests,'login.html')


