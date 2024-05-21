from django.shortcuts import render, redirect, get_object_or_404  # Importing shortcut functions for rendering, redirecting, and getting objects or 404 error
from django.http import HttpResponse, HttpResponseBadRequest  # Importing HTTP response classes
from django.template import loader  # Importing template loader
from .forms import *  # Importing all forms from the current app
from .models import *  # Importing all models from the current app
from .filters import *  # Importing all filters from the current app
from django.contrib.auth import authenticate, login, logout  # Importing authentication functions
from django.contrib.auth.decorators import login_required  # Importing decorator to require login
from django.urls import reverse  # Importing function to reverse URL patterns
from django.contrib import messages  # Importing messages framework to display messages
from django.db.models import Sum  # Importing aggregation function for summing
from django.core.paginator import Paginator  # Importing Paginator for pagination



# Create your views here.
# View for the index page
def index(request):
    template = loader.get_template('index.html')  # Loading the index.html template
    homeContent = template.render()  # Rendering the template
    return HttpResponse(homeContent)  # Returning the rendered template as an HTTP response


# View for the home page, requires login
@login_required
def home(request):
    # Aggregating counts and other data
    count_babies = Babyreg.objects.count()  # Counting all Babyreg objects
    count_sitters = Sitterreg.objects.count()  # Counting all Sitterreg objects
    count_transactions = Payment.objects.count()  # Counting all Payment objects
    recent_babies = Babyreg.objects.all()[:2]  # Getting the two most recent Babyreg objects
    sitters = Sitterreg.objects.all()[:2]  # Getting the two most recent Sitterreg objects
    total_agg = Doll.objects.aggregate(total=Sum('quantity'))  # Summing up the quantity of all Doll objects

    # Creating context dictionary to pass to the template
    context = {
        "count_babies": count_babies,
        "count_sitters": count_sitters,
        "count_dolls_in_stock": total_agg['total'],
        "count_payments": count_transactions,
        "sitters": sitters,
        "recent_babies": recent_babies
    }
    return render(request, 'home.html', context)  # Rendering home.html with the context

#Sitter views
@login_required
def sittersform(request):
    # Paginating the queryset of Sitterreg objects with 5 items per page
    siter = Paginator(Sitterreg.objects.all(), 5)
    page = request.GET.get('page')  # Getting the page number from the request
    sitters = siter.get_page(page)  # Getting the requested page of sitters
    nums = 'k' * sitters.paginator.num_pages  # Generating dummy data for pagination display
    return render(request, 'sittersform.html', {'nums': nums, 'sitters': sitters})

@login_required
def addsitter(request):
    if request.method == 'POST':
        form = Sitterreg_form(request.POST)  # Binding data from POST request to the form
        if form.is_valid():
            form.save()  # Saving the form data to the database
            return redirect('sittersform')  # Redirecting to the sittersform view upon successful submission
        else:
            print("Form is not valid")  # Printing an error message if form validation fails
    else:
        form = Sitterreg_form()  # Creating a new instance of the form for GET requests
    return render(request, 'addsitter.html', {'form': form})  # Rendering the form template

@login_required
def read_sitter(request, id):
    sitters_info = Sitterreg.objects.get(id=id)  # Retrieving sitter details by id
    return render(request, 'read_sitter.html', {'sitters_info': sitters_info})  # Rendering sitter details template


@login_required
def edit_sitter(request, id):
    sitter = get_object_or_404(Sitterreg, id=id)  # Retrieving sitter object by id or 404 if not found
    if request.method == 'POST':
        form = Sitterreg_form(request.POST, instance=sitter)  # Binding data to the form for editing
        if form.is_valid():
            form.save()  # Saving the updated form data
            return redirect('sittersform')  # Redirecting to the sittersform view upon successful submission
        else:
            print("Form is not valid")  # Printing an error message if form validation fails
    else:
        form = Sitterreg_form(instance=sitter)  # Creating a form instance pre-filled with sitter data
    return render(request, 'edit_sitter.html', {'form': form, 'sitter': sitter})  # Rendering edit form template

#view for searching sitters
def search_sitter(request):
    search_query = request.GET.get('search', '')  # Getting the search query from the request
    if search_query:
        sitters = Sitterreg.objects.filter(Sitter_name__icontains=search_query)  # Filtering sitters by name
    else:
        sitters = Sitterreg.objects.all()  # Displaying all sitters if no search query is provided
    return render(request, 'sittersform.html', {'sitters': sitters})  # Rendering sitters template with search results



# View for deleting a sitter
def delete_sitter(request, id):
    if request.user.is_authenticated:  # Checking if user is authenticated
        delete_it = Sitterreg.objects.get(id=id)  # Retrieving sitter object to delete
        delete_it.delete()  # Deleting the sitter from the database
        messages.success(request, "message deleted")  # Displaying success message
        return redirect('sittersform')  # Redirecting to sittersform view after deletion
    else:
        messages.success("you are not authorised")  # Displaying authorization error message
        return redirect('sittersform')  # Redirecting to sittersform view if user is not authorized
    

    
#Sitterpayments
@login_required  # Ensures user authentication
def add_payment(request):
    if request.method == 'POST':  # Checking if the request method is POST
        form = SitterpaymentForm(request.POST)  # Binding data from POST request to the payment form
        if form.is_valid():  
            form.save()  
            return redirect('pay_list')  # Redirecting to the payment list page upon successful form submission
        else:
            print("Form is not valid")  # Printing an error message if form validation fails
    else:
        form = SitterpaymentForm()  # Creating a new instance of the payment form for GET requests
    return render(request, 'add_payment.html', {'form': form})  # Rendering the payment form template



@login_required
def pay_list(request):
    if request.method == 'POST':  # Checking if the request method is POST
        form = SitterpaymentForm(request.POST)  # Binding data from POST request to the payment form
        if form.is_valid():  # Checking if the form data is valid
            form.save()  # Saving the form data to the database
            return redirect('Sitterpaymentform')  # Redirecting to the payment list page upon successful form submission
    else:
        payments = Sitterpayment.objects.all()  # Fetching all payment objects from the database
        form = SitterpaymentForm()  # Creating a new instance of the payment form
    return render(request, 'pay_list.html', {'form': form, 'payments': payments})  # Rendering the payment list template with form and payment data

# View for displaying sitters on duty
@login_required
def onduty(request):
    onduty = Sitter_arrival.objects.all()  # Retrieving all sitter arrival objects
    return render(request, 'onduty.html', {'onduty': onduty})  # Rendering the on duty template with sitter arrival data

# View for adding a sitter's arrival
@login_required
def addonduty(request):
    if request.method == 'POST':  # Checking if the request method is POST
        form = Sitter_arrivalForm(request.POST)  # Binding data from POST request to the sitter arrival form
        if form.is_valid():  # Checking if the form data is valid
            form.save()  # Saving the form data to the database
            return redirect('onduty')  # Redirecting to the onduty view upon successful form submission
        else:
            print("Form is not valid")  # Printing an error message if form validation fails
    else:
        form = Sitter_arrivalForm()  # Creating a new instance of the sitter arrival form for GET requests
    return render(request, 'addonduty.html', {'form': form})  # Rendering the sitter arrival form template

  
@login_required
def editonduty(request, id):
    onduty = get_object_or_404(Sitter_arrival, id=id)  # Retrieving sitter arrival object by id or returning 404 if not found
    if request.method == 'POST':  # Checking if the request method is POST
       form = Sitter_arrivalForm(request.POST, instance=onduty)  # Binding data from POST request to the sitter arrival form for editing
       if form.is_valid(): 
           form.save()  
           return redirect('onduty')  # Redirecting to the onduty view upon successful form submission
    else:
        form = Sitter_arrivalForm(instance=onduty)  # Creating a form instance pre-filled with sitter arrival data
    return render(request,'editonduty.html',{'form':form,'onduty':onduty})  # Rendering the edit sitter arrival form template


# View for deleting a sitter's arrival
@login_required
def delete_onduty(request, id):
    if request.method == 'POST':  # Checking if the request method is POST
        instance = get_object_or_404(Sitter_arrival, id=id)  # Retrieving sitter arrival object by id or returning 404 if not found
        instance.delete()  # Deleting the sitter arrival object from the database
        return redirect('onduty')  # Redirecting to the onduty view after deletion
    else:
        pass  # Placeholder for future actions in case of GET request


#sitter_departure
def sitter_departure(request):
    offduty = Sitter_departure.objects.all()  # Retrieving all sitter departure objects
    return render(request, 'sitter_departure.html', {'offduty': offduty})  # Rendering the sitter departure template with departure data


@login_required
def add_sitter_departure(request):
    if request.method == 'POST':  # Checking if the request method is POST
        form = SitterdepartureForm(request.POST)  # Binding data from POST request to the sitter departure form
        if form.is_valid(): 
            form.save() 
            return redirect('sitter_departure')  # Redirecting to the sitter departure view upon successful form submission
        else:
            print("Form is not valid")  # Printing an error message if form validation fails
    else:
        form = SitterdepartureForm()  # Creating a new instance of the sitter departure form for GET requests
    return render(request, 'add_sitter_departure.html', {'form': form})  # Rendering the sitter departure form template


@login_required
def editoffduty(request, id):
    # Retrieving the sitter departure object by id or returning 404 if not found
    offduty = get_object_or_404(Sitter_departure, id=id)
    if request.method == 'POST':  # Checking if the request method is POST
       form = SitterdepartureForm(request.POST, instance=offduty)  # Binding data from POST request to the sitter departure form for editing
       if form.is_valid():  
           form.save()  
           return redirect('sitter_departure')  # Redirecting to the sitter departure view upon successful form submission
    else:
        form = SitterdepartureForm(instance=offduty)  # Creating a form instance pre-filled with sitter departure data for GET requests
    return render(request,'editoffduty.html',{'form':form,'offduty':offduty})  # Rendering the edit sitter departure form template

# @login_required
# def assign_view(request):
#     assign = Sitter_arrival.objects.all()
#     for assigns in assign:
#         assigns.payment = assigns.babies.all().count() * 3000
#         assigns.save()
#     return render(request, 'assign_view.html',{'assign': assign})  

@login_required
def assign_view(request):
    assign = Sitter_arrival.objects.all()
    for assigns in assign:
        num_babies = assigns.babies.all().count()
        assigns.num_babies = num_babies
        assigns.payment = num_babies * 3000
        assigns.save()
    return render(request, 'assign_view.html', {'assign': assign})


@login_required
def assign_view(request):
    assign = Sitter_arrival.objects.all()
    for assigns in assign:
        num_babies = assigns.babies.all().count()
        assigns.num_babies = num_babies
        assigns.payment = num_babies * 3000
        assigns.save()
        print(f'Sitter: {assigns.sitter_name.Sitter_name}, Babies: {num_babies}, Payment: {assigns.payment}')
    return render(request, 'assign_view.html', {'assign': assign})


@login_required
def assign_sitter(request, id):
    baby = Babyreg.objects.all()  # Retrieving all baby objects
    sitter = Sitterreg.objects.get(id=id)  # Retrieving the sitter object by id
    if request.method == 'POST':  # Checking if the request method is POST
         form = Sitter_arrivalForm(request.POST)  # Binding data from POST request to the sitter arrival form
         if form.is_valid():  
            form.save()  
            return redirect('assign_view')  # Redirecting to the assign view upon successful form submission
         else:
             print("Form is not valid")  # Printing an error message if form validation fails
    else:
        form = Sitter_arrivalForm()  # Creating a new instance of the sitter arrival form for GET requests
    return render(request, 'assign_sitter.html', {'form': form, 'baby':baby, 'sitter':sitter})  # Rendering the assign sitter form template with form, baby, and sitter data




              
#Babies views
@login_required
def babiesform(request):
    # babies= Babyreg.objects.all()
    baby = Paginator(Babyreg.objects.all(), 5)# Retrieving all baby objects and paginating them with 5 items per page
    page = request.GET.get('page') # Getting the current page number from the GET parameters
    babies = baby.get_page(page) # Getting the paginated baby objects for the current page
    nums = 'k' * babies.paginator.num_pages # Creating a string of 'k' characters equal to the number of pages
    return render(request, 'babiesform.html', {'nums': nums, 'babies': babies})# Rendering the babiesform template with the paginated baby objects and page number string


@login_required
def addbaby(request):
    if request.method == 'POST':  # Checking if the request method is POST
        form = Babyreg_form(request.POST)  # Binding data from POST request to the baby registration form
        if form.is_valid(): 
            form.save()  
            return redirect('babiesform')  # Redirecting to the babiesform view upon successful form submission
        else:
            print("Form is not valid")  # Printing an error message if form validation fails
    else:
        form = Babyreg_form()  # Creating a new instance of the baby registration form for GET requests
    return render(request, 'addbaby.html', {'form': form})  # Rendering the baby registration form template

@login_required
def read(request, id):
    # Retrieving the baby object by id
    babies_info = Babyreg.objects.get(id=id)
    # Rendering the read template with the baby details
    return render(request, 'read.html', {'babies_info': babies_info})


@login_required
def edit(request, id):
    # Retrieving the baby object by id or returning 404 if not found
    baby = get_object_or_404(Babyreg, id=id)
    if request.method == 'POST':  # Checking if the request method is POST
        form = Babyreg_form(request.POST, instance=baby)  # Binding data from POST request to the baby registration form for editing
        if form.is_valid():  
            form.save()  
            return redirect('babiesform')  # Redirecting to the babiesform view upon successful form submission
    else:
        form = Babyreg_form(instance=baby)  # Creating a form instance pre-filled with baby data for GET requests
    return render(request, 'edit.html', {'form': form, 'baby': baby})  # Rendering the edit baby form template


@login_required
def delete_baby(request, id):
    if request.user.is_authenticated:  # Checking if the user is authenticated
        # Retrieving the baby object by id
        delete_it = Babyreg.objects.get(id=id)
        delete_it.delete()  # Deleting the retrieved baby object from the database
        # Displaying a success message indicating that the baby record has been deleted
        messages.success(request, "message deleted")
        # Redirecting to the babiesform view after successful deletion
        return redirect('babiesform')
    else:
        # Displaying an error message indicating that the user is not authorized to delete the record
        messages.success(request, "you are not authorised")
        # Redirecting to the babiesform view if the user is not authorized
        return redirect('babiesform')

    
#Babies payments
@login_required  
def payment(request):
    if request.method == 'POST':  # Checking if the request method is POST
        form = PaymentForm(request.POST)  # Binding data from POST request to the payment form
        if form.is_valid():  
            form.save()  
            # Redirecting to the payment list page upon successful form submission
            return redirect('paymentform')
    else:
        payments = Payment.objects.all()  # Retrieving all payment objects
        form = PaymentForm()  # Creating a new instance of the payment form for GET requests
    
    # Rendering the payment form template with form and payments data
    return render(request, 'paymentform.html', {'form': form, 'payments': payments})

@login_required
def all_payments(request):
    payments = Payment.objects.all()  # Retrieving all payment objects
    # Calculating the total amount paid
    total = sum([items.amount_paid for items in payments])
    # Calculating the total balance
    balance = sum([items.get_balance() for items in payments])
    # Calculating the net amount (total amount paid + balance)
    net = total + balance
    # Rendering the payment form template with payments, total, balance, and net data
    return render(request, 'paymentform.html', {'payments': payments, 'total': total, 'balance': balance, 'net': net})


@login_required  
def addpayment(request):
    if request.method == 'POST':  # Checking if the request method is POST
        form = PaymentForm(request.POST)  # Binding data from POST request to the payment form
        if form.is_valid():  # Checking if the form data is valid
            form.save()  
            print(form)  
            return redirect('paymentform')  # Redirecting to the payment list page upon successful form submission
        else:
            print("Form is not valid")  # Printing an error message if form validation fails
    else:
        form = PaymentForm()  # Creating a new instance of the payment form for GET requests
    # Rendering the add payment form template with form data
    return render(request, 'addpayment.html', {'form': form})


@login_required  
def editpayment(request, id):
    # Retrieving the payment object by id or returning 404 if not found
    payment = get_object_or_404(Payment, id=id)
    
    if request.method == 'POST':  # Checking if the request method is POST
        form = PaymentForm(request.POST, instance=payment)  # Binding data from POST request to the payment form for editing
        if form.is_valid():  
            form.save()  
            return redirect('paymentform')  # Redirecting to the payment list page after editing payment
    else:
        form = PaymentForm(instance=payment)  # Creating a form instance pre-filled with payment data for GET requests
    
    # Rendering the edit payment form template with form and payment data
    return render(request, 'editpayment.html', {'form': form, 'payment': payment})



@login_required  
def search_baby(request):
    query = request.GET.get('search')  # Getting the search query from the GET parameters
    # Filtering Babyreg objects based on the search query, matching Baby_name case insensitively
    babies = Babyreg.objects.filter(Baby_name__icontains=query)
    # Rendering the babiesform template with the filtered baby objects
    return render(request, 'babiesform.html', {'babies': babies})

@login_required  
def departure(request):
    babies = Departure.objects.all()  # Retrieving all departure objects
    # Rendering the departure template with the list of departure objects
    return render(request, 'departure.html', {'babies': babies})

@login_required  
def adddeparture(request):
    if request.method == 'POST':  # Checking if the request method is POST
        form = DepartureForm(request.POST)  # Binding data from POST request to the departure form
        if form.is_valid():  # Checking if the form data is valid
            form.save()  
            print(form)  # Printing the form data (for debugging purposes)
            return redirect('departure')  # Redirecting to the departure list page upon successful form submission
        else:
            print("Form is not valid")  # Printing an error message if form validation fails
    else:
        form = DepartureForm()  # Creating a new instance of the departure form for GET requests
    # Rendering the add departure form template with form data
    return render(request, 'adddeparture.html', {'form': form})


@login_required 
def editdeparture(request, id):
    # Retrieving the departure object by id or returning 404 if not found
    departures = get_object_or_404(Departure, id=id)
    if request.method == 'POST':  # Checking if the request method is POST
        form = DepartureForm(request.POST, instance=departures)  # Binding data from POST request to the departure form for editing
        if form.is_valid():  
            form.save()  # Saving the updated form data to the database
            return redirect('departure')  # Redirecting to the departure list page after editing departure
    else:
        form = DepartureForm(instance=departures)  # Creating a form instance pre-filled with departure data for GET requests
    # Rendering the edit departure form template with form and departure data
    return render(request, 'editdeparture.html', {'form': form, 'departures': departures})



#Dolls Views
@login_required
def search_doll(request):
    query = request.GET.get('search')  # Getting the search query from the GET parameters
    # Filtering Doll objects based on the search query, matching name_of_the_doll case insensitively
    dolls = Doll.objects.filter(name_of_the_doll__icontains=query)
    # Rendering the doll template with the filtered doll objects
    return render(request, 'doll.html', {'dolls': dolls})



@login_required  
def doll(request):
    dolls = Doll.objects.all()  # Retrieving all doll objects
    # Rendering the doll template with the list of doll objects
    return render(request, 'doll.html', {'dolls': dolls})

@login_required  
def dollcorner(request, doll_id):
    doll = get_object_or_404(Doll, id=doll_id)  # Retrieving the doll object by id or returning 404 if not found
    # Rendering the dollcorner template with the doll object
    return render(request, 'dollcorner.html', {'doll': doll})


@login_required  
def issue_item(request, pk):
    issued_item = Doll.objects.get(id=pk)  # Retrieving the doll object by id
    sales_form = SalesrecordForm(request.POST)  # Binding data from POST request to the sales record form

    if request.method == 'POST':  # Checking if the request method is POST
        if sales_form.is_valid():  # Checking if the sales form data is valid
            new_sale = sales_form.save(commit=False)  # Creating a new sale record without saving it to the database yet
            new_sale.doll = issued_item  # Associating the sale record with the issued doll
            new_sale.unit_price = issued_item.Unit_price  # Setting the unit price for the sale record
            new_sale.save()  # Saving the sale record to the database
            issued_quantity = int(request.POST['quantity_sold'])  # Getting the quantity sold from the POST data
            issued_item.quantity -= issued_quantity  # Reducing the quantity of the doll by the issued quantity
            issued_item.save()  # Saving the updated doll object to the database
            print(issued_item.name_of_the_doll)  # Printing the name of the doll (for debugging purposes)
            print(request.POST['quantity_sold'])  # Printing the quantity sold (for debugging purposes)
            print(issued_item.quantity)  # Printing the remaining quantity of the doll (for debugging purposes)
            return redirect('receipt')  # Redirecting to the receipt page upon successful form submission
    # Rendering the issue item template with the sales form
    return render(request, 'issue_item.html', {'sales_form': sales_form})



@login_required  
def receipt(request):
    sales = Salesrecord.objects.all().order_by('id')  # Retrieving all sales records ordered by their id
    # Rendering the receipt template with the list of sales records
    return render(request, 'receipt.html', {'sales': sales})


@login_required  
def receipt_detail(request, receipt_id):
    # Retrieving the sales record by id
    receipt = Salesrecord.objects.get(id=receipt_id)
    # Rendering the receipt detail template with the sales record object
    return render(request, 'receipt_detail.html', {'receipt': receipt})


@login_required 
def add_to_stock(request, pk):
    issued_item = Doll.objects.get(id=pk)  # Retrieving the specific doll item by id from the database
    if request.method == 'POST':  # Checking if the request method is POST
        form = Addform(request.POST)  # Binding data from POST request to the add form
        if form.is_valid():  # Checking if the form data is valid
            received_quantity = request.POST.get('received_quantity')  # Getting the received quantity from the form data
            if received_quantity:  # Checking if received quantity is provided
                try:
                    added_quantity = int(received_quantity)  # Converting the received quantity to an integer
                    issued_item.quantity += added_quantity  # Adding the received quantity to the existing stock quantity
                    issued_item.save()  # Saving the updated doll item to the database
                    print(added_quantity)  # Printing the added quantity (for debugging purposes)
                    print(issued_item.quantity)  # Printing the updated quantity of the doll (for debugging purposes)
                    return redirect('doll')  # Redirecting to the doll page upon successful form submission
                except ValueError:  # Handling the case where the received quantity is not a valid integer
                    return HttpResponseBadRequest("Invalid quantity")  # Returning a bad request response with an error message
            else:
                print("Form is not valid")  # Printing a message if the form data is not valid (for debugging purposes)
    else:
        form = Addform()  # Creating a new, empty add form
    # Rendering the add_to_stock template with the add form
    return render(request, 'add_to_stock.html', {'form': form})



@login_required  
def all_sales(request):
    sales = Salesrecord.objects.all()  # Retrieving all sales records
    total = sum([items.amount_received for items in sales])  # Calculating the total amount received from all sales
    change = sum([items.get_change() for items in sales])  # Calculating the total change given for all sales
    net = total - change  # Calculating the net amount received (total received - total change)
    # Rendering the all_sales template with the sales records, total amount received, total change, and net amount
    return render(request, 'all_sales.html', {'sales': sales, 'total': total, 'change': change, 'net': net})

# Procurement Views
@login_required  # Ensures user authentication
def inventory(request):
    inventories = Procurement.objects.all()  # Retrieving all procurement (inventory) records
    # Rendering the inventory template with the inventory records
    return render(request, 'inventory.html', {'inventories': inventories})


@login_required  # Ensures user authentication
def add_to_stocks(request, pk):
    issued_procurement = Procurement.objects.get(id=pk)  # Retrieving the specific procurement item by id
    if request.method == 'POST':  # Checking if the request method is POST
        form = AddForm(request.POST)  # Binding data from POST request to the add form
        if form.is_valid():  # Checking if the form data is valid
            received_quantity = form.cleaned_data.get('received_quantity')  # Getting the received quantity from the form data
            added_quantity = int(received_quantity)  # Converting the received quantity to an integer
            issued_procurement.Quantity += added_quantity  # Adding the received quantity to the existing stock quantity
            issued_procurement.save()  # Saving the updated procurement item to the database
            return redirect('inventory')  # Redirecting to the inventory page upon successful form submission
        else:
            print("Form is not valid")  # Printing a message if the form is not valid 
    else:
        form = AddForm()  # Creating a new, empty add form
    # Rendering the add_to_stocks template with the add form
    return render(request, 'add_to_stocks.html', {'form': form})


    

@login_required  
def issue(request, pk):
    issued_item = Procurement.objects.get(id=pk)  # Retrieving the procurement item by id
    issue_form = Usedform(request.POST)  # Binding data from POST request to the used form

    if request.method == 'POST':  # Checking if the request method is POST
        if issue_form.is_valid():  # Checking if the issue form data is valid
            new_issue = issue_form.save(commit=False)  # Creating a new issue record without saving it to the database yet
            new_issue.item = issued_item  # Associating the issue record with the procured item
            new_issue.save()  # Saving the issue record to the database
            issued_quantity = int(request.POST['quantity_issued'])  # Getting the issued quantity from the POST data
            issued_item.Quantity -= issued_quantity  # Reducing the quantity of the procured item by the issued quantity
            issued_item.save()  # Saving the updated procurement item to the database
            print(issued_item.item_name)  # Printing the name of the issued item 
            print(request.POST['quantity_issued'])  # Printing the issued quantity 
            print(issued_item.Quantity)  # Printing the remaining quantity of the item 
            return redirect('inventory')  # Redirecting to the inventory page upon successful form submission
    # Rendering the issue template with the issue form
    return render(request, 'issue.html', {'issue_form': issue_form})


@login_required  # Ensures user authentication
def all_issue_items(request):
    issues = Used.objects.all()  # Retrieving all used (issued) items
    # Aggregating the total issued quantity
    total_issued_quantity = issues.aggregate(total_issued_quantity=Sum('quantity_issued'))['total_issued_quantity'] or 0
    # Aggregating the total received quantity
    total_received_quantity = Procurement.objects.aggregate(total_received_quantity=Sum('Quantity'))['total_received_quantity'] or 0
    # Calculating the net quantity (received quantity - issued quantity)
    net_quantity = total_received_quantity - total_issued_quantity
    # Rendering the all_issue_items template with the issues, total issued quantity, total received quantity, and net quantity
    return render(request, 'all_issue_items.html', {'issues': issues, 'total_issued_quantity': total_issued_quantity, 'total_received_quantity': total_received_quantity, 'net_quantity': net_quantity})
