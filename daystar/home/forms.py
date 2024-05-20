from django.forms import ModelForm
from .models import *
from django import forms

# Create your forms here.
class Sitterreg_form(forms.ModelForm):
    class Meta:
        model = Sitterreg
        fields = '__all__'
        # Widget to customize the date input field as a datetime-local input
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            # 'Date_of_birth': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
       

class Babyreg_form(forms.ModelForm):
    class Meta:
        model = Babyreg
        fields = '__all__'
        # Widget to customize the Date input field as a datetime-local input
        widgets = {
            'Date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
class DollForm(ModelForm):
    class Meta:
        model = Doll
        fields = '__all__'
        
class Addform(ModelForm):
    class Meta:
        model = Doll
        fields = ['received_quantity']
        
class SalesrecordForm(ModelForm):
    class Meta:
        model = Salesrecord
        fields = ['quantity_sold', 'amount_received', 'payee']
        
class AddForm(ModelForm):
    class Meta:
        model = Procurement
        fields = ['received_quantity']
        

class Usedform(ModelForm):
    class Meta:
        model = Used
        fields = '__all__'
        

class PaymentForm(ModelForm):
    # Define a form for the Payment model
    class Meta:
        # Specify the model that the form is based on
        model = Payment
        # Define the fields to be included in the form
        fields = ['payee', 'c_payment', 'c_mode', 'selected_amount', 'amount_paid', 'payment_status']
        # Comment: The form includes fields for payee, payment category, payment mode, selected amount,
        # amount paid, and payment status.

class SitterpaymentForm(ModelForm):
    class Meta:
        # Specify the model that the form is based on
        model = Sitterpayment
        # Define all fields of the model to be included in the form
        fields = '__all__'
        

        
class DepartureForm(ModelForm):
    class Meta:
        model = Departure
        fields = ['baby_name', 'date', 'picker', 'contact', 'NIN', 'comment']
        # Widget to customize the date input field as a datetime-local input
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }
        

class Sitter_arrivalForm(ModelForm):
    class Meta:
        model = Sitter_arrival
        fields = ['date_of_arrival', 'sitter_name', 'babies', 'Attendancestatus']
        # Widgets to customize the babies field as a CheckboxSelectMultiple and date_of_arrival as a datetime-local input
        widgets = {
            'babies': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
            'date_of_arrival': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
       

class SitterdepartureForm(forms.ModelForm):
    class Meta:
        model = Sitter_departure
        fields = ['sitter', 'sitter_number', 'departure_time', 'comment']
        # Widget to customize the departure_time input field as a datetime-local input
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
