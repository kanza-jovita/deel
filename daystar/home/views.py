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



   

# Create your views here.
def index(request):
        template = loader.get_template('index.html')
        homeContent = template.render()
        return HttpResponse(homeContent)

@login_required
def dash(request):
        template = loader.get_template('base.html')
        return HttpResponse(template.render())


@login_required
def payments(request):
        template = loader.get_template('payments.html')
        return HttpResponse(template.render())


@login_required
def dolls(request):
        template = loader.get_template('dolls.html')
        return HttpResponse(template.render())


# @login_required
# def procurement(request):
#         template = loader.get_template('procurement.html')
#         return HttpResponse(template.render())


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


@login_required
def procurement(request):
    query = request.GET.get('q')

    products = Product.objects.all().order_by('-id')

    if query:
        products = products.annotate(search=SearchVector('product_name')).filter(search=query)

    product_filters = ProductFilter(request.GET, queryset=products)
    products = product_filters.qs

    return render(request, 'procurement.html', {'products': products, 'product_filters': product_filters})



@login_required
def product_detail(request,product_id):
    product=Product.objects.get(id=product_id)
    return render(request,'product_detail.html',{'product':product})

    

 # this retrieves a list of sales records from the database and then orders them by id.
 # and renders the receipt.html template which is responsible for displaying a list of sales receipts. 
@login_required
def receipt(request):
    sales=Sale.objects.all().order_by('-id')
    return render(request,'receipt.html',{'sales':sales})


# this handles the issuing of an item for sale.
# it fetches the specific product using pk and processes the sale using SaleForm.
# after a successful sale it redirects you to the receipt view.

@login_required 
def issue_item(request,pk):
    issued_item=Product.objects.get(id=pk)
    sales_form=SaleForm(request.POST)

    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale=sales_form.save(commit=False)
            new_sale.item=issued_item
            new_sale.unit_price=issued_item.unit_price
            new_sale.save()
            #keeping track of the stock remaining after sale.
            issued_quantity=int(request.POST['quantity'])
            issued_item.total_quantity-=issued_quantity
            issued_item.save()

            print(issued_item.product_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity)

            return redirect('receipt')
    return render(request, 'issue_item.html',{'sales_form':sales_form})


    
# This fetches sales receipt from the database based on receipt id parameter.
# then renders a receipt_detail.html displaying detailed informtion about a selected receipt.
@login_required
def receipt_detail(request,receipt_id):
    # below is a query.
    # here we are querying all the data by id.
    receipt=Sale.objects.get(id=receipt_id)
    return render(request,'receipt_detail.html',{'receipt':receipt})


# This list retrieves a list of all sales records from the db and then calculates
# the total,change and net values based on the sales data.
# the results are then rendered in the all_sales.html template.
@login_required
def all_sales(request):
    # query all the data from the module Sale below on line 85.
    sales=Sale.objects.all()
    total=sum([items.amount_received for items in sales])
    change=sum([items.get_change() for items in sales])
    net=total-change
    return render(request, 'all_sales.html',{'sales':sales, 'total':total, 'change':change, 'net':net})



# This handles the process of adding items to the stock.
# it fetches a product using its pk and processes the addition using the AddForm and updates the stock of the product.
# After a successful adding of stock, it redirecs you to the home view.
@login_required
def add_to_stock(request,pk):
    issued_item=Product.objects.get(id=pk)
    form=AddForm(request.POST)

    if request.method=='POST':
        if form.is_valid():
            added_quantity=int(request.POST['received_quantity'])
            issued_item.total_quantity += added_quantity
            issued_item.save()
            # to add to the remaining stock quantity is reduced.
            print(added_quantity)
            print(issued_item.total_quantity)
            return redirect('procurement')
    return render(request, 'add_to_stock.html', {'form': form})

# Create your views here.
# a view is a function that responds to a url request.
# defined function must have different names.










