from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from myapp.form import addmedicine,addcustomer,adddealer,addpurchase
from .models import medicine,dealer,customer,purchase
from django.contrib.auth.decorators import login_required








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
           return redirect('view_medicine')
       else:
           messages.info(request,'Username or password is invalid!!')
           return redirect("login")
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')
        
@login_required
def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')

    else:
        return redirect(login)
    
    # add a items function
@login_required
def add_medicine(request):
    addmedicines = addmedicine()
    if request.method == 'POST':
        addmedicines = addmedicine(request.POST)
        if addmedicines.is_valid():
            addmedicines.save()
            return redirect('add_medicine')
    return render(request,'addvalues/add_medicine.html',{'addmedicines':addmedicines})
@login_required
def add_customer(request):
    addcustomers = addcustomer()
    if request.method == 'POST':
        addcustomers = addcustomer(request.POST)
    if addcustomers.is_valid():
        addcustomers.save()
        return redirect('add_customer')
    return render(request,'addvalues/add_customer.html',{'addcustomers':addcustomers})
@login_required
def add_dealer(request):
    adddealers = adddealer()
    if request.method == 'POST':
        adddealers = adddealer(request.POST)
        if adddealers.is_valid():
            adddealers.save()
            return redirect('add_dealer')
    return render(request,'addvalues/add_dealer.html',{'adddealers':adddealers})

@login_required
def add_purchase(request):
    addpurchases = addpurchase()
    if request.method == 'POST':
        addpurchases = addpurchase(request.POST)
        if addpurchases.is_valid():
            addpurchases.save()
            return redirect('add_purchase')
    return render(request,'addvalues/add_purchase.html',{'addpurchases':addpurchases})


@login_required
# update values 
def update_medicine(request, id):
    medicines = medicine.objects.get(id=id)
    
    if request.method == 'POST':
        name = request.POST['name'] 
        company = request.POST['company'] 
        cost = request.POST['cost'] 
        type = request.POST['type'] 

        medicines.name =name
        medicines.company =company
        medicines.cost = cost
        medicines.type= type 
        medicines.save()
        return redirect('/view_medicine')
    return render(request,'updatefiles/update_medicine.html', {'medicines':medicines})

def update_customer(request, id):
    customers = customer.objects.get(id=id)
    
    if request.method == 'POST':
        cus_name = request.POST['cus_name'] 
        address = request.POST['address'] 
        phone_no = request.POST['phone_no'] 
        email = request.POST['email'] 

        customers.cus_name =cus_name
        customers.address =address
        customers.phone_no = phone_no
        customers.email= email 
        customers.save()
        return redirect('/view_customer')
    return render(request,'updatefiles/update_customer.html', {'customers':customers})

def update_dealer(request, id):
    dealers = dealer.objects.get(id=id)
    
    if request.method == 'POST':
        med_name = request.POST['med_name'] 
        dealer_nam = request.POST['dealer_nam'] 
        cost = request.POST['cost'] 
        stock = request.POST['stock'] 
        Description = request.POST['Description'] 

        dealers.med_name =med_name
        dealers.dealer_nam = dealer_nam
        dealers.cost = cost
        dealers.stock = stock
        dealers.Description = Description
        dealers.save()
        return redirect('/view_customer')
    return render(request,'updatefiles/update_dealer.html', {'dealers':dealers})

def update_purchase(request,id):
    purchases = purchase.objects.get(id=id)
    
    if request.method == 'POST':
        product_name = request.POST['product_name'] 
        price =request.POST['price'] 
        quantity = request.POST['quantity'] 
    

        purchases.product_name =product_name
        purchases.price = price
        purchases.quantity = quantity
        purchases.save()
        return redirect('/view_purchase')
    return render(request,'updatefiles/update_purchase.html', {'purchases':purchases})
#view a items functions
@login_required
def view_medicine(request):
     if 'search' in request.GET:
         search = request.GET['search']
         medicines = medicine.objects.filter(name__icontains = search)
     else:
         
        medicines = medicine.objects.all()
     return render(request,'viewfiles/view_medicine.html',{"medicine": medicines})
  
@login_required
def view_dealer(request):
    if 'search' in request.GET:
        search = request.GET['search']
        dealers = dealer.objects.filter(dealer_nam__icontains = search)
    else:
        dealers = dealer.objects.all()
    return render(request,'viewfiles/view_dealer.html',{"dealers": dealers})
       
@login_required 
def view_customer(request):
    if 'search' in request.GET:
        search = request.GET['search']
        customers = customer.objects.filter(cus_name__icontains = search)
    else:
        customers = customer.objects.all()
    return render(request,'viewfiles/view_customer.html',{"customer": customers})
       
@login_required
def view_purchase(request):
    if 'search' in request.GET:
        search = request.GET['search']
        purchases = purchase.objects.filter(product_name__icontains = search)
    else:
        purchases = purchase.objects.all()
    return render(request,'viewfiles/view_purchase.html',{"purchases": purchases})
     
      
@login_required  
def delete_med(request,id):
        medicines = medicine.objects.get(id=id)
        medicines.delete()
        return redirect('/view_medicine')
@login_required  
def delete_purchase(request,id):
        purchases = purchase.objects.get(id=id)
        purchases.delete()
        return redirect('/view_purchase')
def delete_customer(request,id):
        customers = customer.objects.get(id=id)
        customers.delete()
        return redirect('/view_customer')
def delete_dealer(request,id):
        dealers = dealer.objects.get(id=id)
        dealers.delete()
        return redirect('/view_dealer')









   
    
    


    
     



 



  



    # return render(requests,'login.html')


