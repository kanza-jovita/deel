from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader 
from .forms import * 
from .models import *
from .filters import *
from django.contrib.auth import authenticate,login  
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django.db.models import Sum



# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    homeContent = template.render()
    return HttpResponse(homeContent)

@login_required
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def payment(request):
    template = loader.get_template('payment.html')
    return HttpResponse(template.render())


#Sitter views
@login_required
def addsitter(request):
    if request.method == 'POST':
        form = Sitterreg_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sittersform')
    else:
        form=Sitterreg_form()
    return render(request,'addsitter.html',{'form':form})


@login_required
def sittersform(request):
    sitters= Sitterreg.objects.all()
    return render(request,'sittersform.html',{'sitters':sitters})

    

@login_required
def read_sitter(request,id ):
    sitters_info=Sitterreg.objects.get(id=id)
    return render(request,'read_sitter.html',{'sitters_info':sitters_info})
@login_required
def edit_sitter(request,id):
    sitter=get_object_or_404(Sitterreg,id=id)
    if request.method == 'POST':
        form=Sitterreg_form (request.POST,instance=sitter)
        if form.is_valid():
            form.save()
            return redirect('sittersform')
    else:
            form =Sitterreg_form(instance=sitter)
    return render(request,'edit_sitter.html',{'form':form,sitter:sitter})


def search_sitter(request):
    search_query = request.GET.get('search', '')
    if search_query:
        sitters = Sitterreg.objects.filter(Sitter_name__icontains=search_query) | Sitterreg.objects.filter(Siiter_number__icontains=search_query)
    else:
        sitters = Sitterreg.objects.all()

    return render(request, 'siitersform.html', {'sitters': sitters})
            
      
#Babies views
@login_required
def babiesform(request):
      babies= Babyreg.objects.all()
      return render(request,'babiesform.html',{'babies':babies})

@login_required
def addbaby(request):
    if request.method == 'POST':
        form = Babyreg_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('babiesform')
    else:
        form=Babyreg_form()
    return render(request,'addbaby.html',{'form':form})


@login_required
def read(request,id ):
    babies_info=Babyreg.objects.get(id=id)
    return render(request,'read.html',{'babies_info':babies_info})


@login_required
def edit(request,id):
    baby=get_object_or_404(Babyreg,id=id)
    if request.method == 'POST':
        form=Babyreg_form (request.POST,instance=baby)
        if form.is_valid():
            form.save()
            return redirect('babiesform')
    else:
            form =Babyreg_form(instance=baby)
    return render(request,'edit.html',{'form':form,baby:baby})


def delete_baby (request, id):
    if request.user.is_authenticated:
        delete_it = Babyreg.objects.get(id=id)
        delete_it.delete()
        messages.success(request, "message deleted")
        return redirect('babiesform')
    else:
        messages.success("you are not authorised")
        return redirect('babiesform')


def search_baby(request):
    search_query = request.GET.get('search', '')
    if search_query:
        babies = Babyreg.objects.filter(Baby_name__icontains=search_query) | Babyreg.objects.filter(Baby_number__icontains=search_query)
    else:
        babies = Babyreg.objects.all()

    return render(request, 'babiesform.html', {'babies': babies})


           

     


# @login_required
# def procurement(request):
#     query = request.GET.get('q')

#     products = Product.objects.all().order_by('-id')

#     if query:
#         products = products.annotate(search=SearchVector('product_name')).filter(search=query)

#     product_filters = ProductFilter(request.GET, queryset=products)
#     products = product_filters.qs

#     return render(request, 'procurement.html', {'products': products, 'product_filters': product_filters})



#Dolls Views
def dollcorner(request, doll_id):
    doll = get_object_or_404(Doll, id=doll_id)
    return render(request, 'dollcorner.html', {'doll': doll})

@login_required
def issue_item(request,pk):
    issued_item=Doll.objects.get(id=pk) 
    sales_form=SalesrecordForm(request.POST)  

    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale=sales_form.save(commit=False)
            new_sale.doll=issued_item
            new_sale.unit_price=issued_item.Unit_price
            new_sale.save()
            issued_quantity=int(request.POST['quantity_sold'])
            issued_item.quantity-=issued_quantity
            issued_item.save()
            print(issued_item.name_of_the_doll)
            print(request.POST['quantity_sold'])
            print(issued_item.quantity)
            return redirect('receipt')
    return render(request, 'issue_item.html',{'sales_form':sales_form} )

@login_required
def receipt(request):
    sales= Salesrecord.objects.all().order_by('-id') 
    return render(request,'receipt.html',{'sales':sales})  

@login_required
def receipt_detail(request, receipt_id):
    receipt = Salesrecord.objects.get(id=receipt_id)
    return render(request,'receipt_detail.html',{'receipt':receipt})


@login_required
def add_to_stock(request, pk):
    issued_item = Doll.objects.get(id=pk)
    if request.method == 'POST':
        form = Addform(request.POST)
        if form.is_valid():
            received_quantity = request.POST.get('received_quantity')
            if received_quantity:
                try:
                    added_quantity = int(received_quantity)
                    issued_item.quantity += added_quantity
                    issued_item.save()
                    print(added_quantity)
                    print(issued_item.quantity)
                    return redirect('doll')
                except ValueError:
                    return HttpResponseBadRequest("Invalid quantity")
    else:
        form = Addform()
    return render(request, 'add_to_stock.html', {'form': form})

def add_to_stock(request,pk):
    issued_item=Doll.objects.get(id=pk)
    form=Addform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            added_quantity=int(request.POST['received_quantity'])
            issued_item.quantity+=added_quantity
            issued_item.save()
            print(added_quantity)
            print(issued_item.quantity)
            return redirect('doll')
    return render(request, 'add_to_stock.html',{'form':form})

@login_required
def all_sales(request):
    sales=Salesrecord.objects.all()
    total=sum([items.amount_received for items in sales])
    change=sum([items.get_change() for items in sales])
    net=total-change
    return render(request,'all_sales.html',{'sales':sales,'total':total,'change':change,'net':net})

@login_required
def doll(request):
    dolls=Doll.objects.all()
    return render(request,'doll.html',{'dolls':dolls})

#Procurement
@login_required
def add_to_stocks(request, pk):
    issued_procurement = Procurement.objects.get(id=pk)
    
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            received_quantity = form.cleaned_data.get('received_quantity')
            added_quantity = int(received_quantity)
            issued_procurement.Quantity += added_quantity

            issued_procurement.save()
            return redirect('inventory')  
    else:
        form = AddForm()
    
    return render(request, 'add_to_stocks.html', {'form': form})

@login_required
def inventory(request):
    inventories=Procurement.objects.all()
    return render(request,'inventory.html',{'inventories':inventories})
    
def issue(request, pk):
    issued_item = Procurement.objects.get(id=pk) 
    issue_form = Usedform(request.POST)  

    if request.method == 'POST':
        if issue_form.is_valid():
            new_issue = issue_form.save(commit=False)
            new_issue.item = issued_item
            new_issue.save()
            issued_quantity = int(request.POST['quantity_issued'])
            issued_item.Quantity -= issued_quantity

            issued_item.save()
            print(issued_item.item_name)
            print(request.POST['quantity_issued'])
            print(issued_item.Quantity)
            return redirect('inventory')
    return render(request, 'issue.html', {'issue_form': issue_form})

@login_required
def all_issue_items(request):
    issues = Used.objects.all()
    total_issued_quantity = issues.aggregate(total_issued_quantity=Sum('quantity_issued'))['total_issued_quantity'] or 0
    total_received_quantity = Procurement.objects.aggregate(total_received_quantity=Sum('Quantity'))['total_received_quantity'] or 0
    net_quantity = total_received_quantity - total_issued_quantity
    return render(request, 'all_issue_items.html', {'issues': issues, 'total_issued_quantity': total_issued_quantity, 'total_received_quantity': total_received_quantity, 'net_quantity': net_quantity})


#Payments
def paymentform(request):
    payment= Payment.objects.all()
    return render(request,'paymentform.html',{'payment':payment})
    

def addpayment(request):
    if request.method=='POST':
        form=PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('paymentform')
    else:
        form=PaymentForm()
    return render(request,'addpayment.html',{'form':form})
    


def editpayment(request, id):
    payment = get_object_or_404(Payment, id=id)
    
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('paymentlist')  # Redirect to the payment list page after editing payment
    else:
        form = PaymentForm(instance=payment)
    
    return render(request, 'editpayment.html', {'form': form, 'payment': payment})


def paymentlist(request):
    payments=Payment.objects.all()
    return render(request,'paymentlist.html',{'payments':payments})

def createpayment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paymentlist') 
    else:
        form = PaymentForm()
    
    return render(request, 'createpayment.html', {'form': form})



#Sitterpayment
def create_payment(request):
    if request.method == 'POST':
        form = SitterpaymentForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('payment_list')
    else:
        form = SitterpaymentForm()
    

    return render(request, 'create_payment.html', {'form': form})


def payment_list(request):
  payments=Sitterpayment.objects.all()
  return render(request,'payment_list.html',{'payments':payments})

#Arrivals and departures
def arrival(request):
    arrivals=Arrival.objects.all()
    return render(request,'arrival.html',{'arrivals':arrivals})
  
def addarrival(request):
      if request.method=='POST':
        form=ArrivalForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('arrival')
      else:
        form=ArrivalForm()
      return render(request,'addarrival.html',{'form':form })         
  

def editarrival(request,id):
     arrivals=get_object_or_404(Arrival,id=id)
     if request.method == 'POST':  
       form=ArrivalForm(request.POST,instance=arrivals)
       if form.is_valid():
           form.save()
           return redirect('arrival')
     else:
            form=ArrivalForm(instance=arrivals) 
     return render(request,'editarrival.html',{'form':form,'arrivals':arrivals})     

def departure(request):
  babys=Departure.objects.all()
  return render(request,'departure.html',{'babys':babys})


def adddeparture(request):
   if request.method=='POST':
        form=DepartureForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('departure')
   else:
            form=DepartureForm()
   return render(request,'adddeparture.html',{'form':form })      
  

def editdeparture(request,id):
     departures=get_object_or_404(Departure,id=id)
     if request.method == 'POST':  
       form=DepartureForm(request.POST,instance=departures) 
       if form.is_valid():
           form.save()
           return redirect('departure')
     else:
            form=DepartureForm(instance=departures) 
     return render(request,'editdeparture.html',{'form':form,'departures':departures})     



def onduty(request):
  onduty=Sitter_arrival.objects.all()
  return render(request,'onduty.html',{'onduty':onduty})
  return render(request,'onduty.html')

def addonduty(request):
   if request.method=='POST':
        form=Sitter_arrivalForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('onduty')
   else:
            form=DepartureForm()
   return render(request,'addsonduty.html',{'form':form })      
  

def readonduty(request):
   baby_info=Payment.objects.get(id=id)
   return render(request,'readonduty.html')

def editonduty(request):
    departures=get_object_or_404(Departure,id=id)
    if request.method == 'POST':  
       form=DepartureForm(request.POST,instance=arrival)
       if form.is_valid():
           form.save()
           return redirect('onduty')
    else:
            form=DepartureForm(instance=departures) 
    return render(request,'editsarrval.html',{'form':form,'departures':departure})     


 


  







 
