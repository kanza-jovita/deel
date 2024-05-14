from django.forms import ModelForm
from .models import *
from django import forms

# Create your forms here.
class Sitterreg_form(forms.ModelForm):
    class Meta:
        model = Sitterreg
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        

class Babyreg_form(forms.ModelForm):
    class Meta:
        model = Babyreg
        fields = '__all__'
        widgets = {
            'Date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        


class  DollForm(ModelForm):
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
        fields = [ 'quantity_sold', 'amount_received', 'payee']  


# class Departure_form(ModelForm):
#     class Meta:
#         model = Departure
#         fields = '__all__'
#         widgets = {
#             'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }

class AddForm(ModelForm):
     class Meta:
         model=Procurement
         fields=['received_quantity']  

class Usedform(ModelForm):
     class Meta:
         model=Used
         fields='__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['payee', 'c_payment','c_mode', 'selected_amount','amount_paid','payment_status'] 

class SitterpaymentForm(ModelForm):
     class Meta:
         model=Sitterpayment
         fields='__all__'


class   DepartureForm(ModelForm):
     class Meta:
         model=Departure
         fields= ['baby_name', 'date', 'picker', 'contact', 'NIN', 'comment']
         widget = {
               'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
         }


class Sitter_arrivalForm(ModelForm):
     class Meta:
         model=Sitter_arrival
         fields=['date_of_arrival', 'sitter_name', 'babies', 'Attendancestatus']
         widgets = {
            'babies':forms.CheckboxSelectMultiple(attrs={'class':'checkbox'}),
            'date_of_arrival': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }  




class SitterdepartureForm(forms.ModelForm):
    class Meta:
        model = Sitter_departure
        fields = ['sitter', 'departure_time', 'comment'] 
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
          
         