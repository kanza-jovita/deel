from django.forms import ModelForm
from .models import *
from django import forms

# Create your forms here.
class Sitterreg_form(forms.ModelForm):
    class Meta:
        model = Sitterreg
        fields = '__all__'

class Babyreg_form(forms.ModelForm):
    class Meta:
        model = Babyreg
        fields = '__all__'


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



class Arrival_form(forms.ModelForm):
    class Meta:
        model = Arrival
        fields = '__all__'


class Departure_form(ModelForm):
    class Meta:
        model = Departure
        fields = '__all__'


class AddForm(ModelForm):
     class Meta:
         model=Procurement
         fields=['received_quantity']  

class Usedform(ModelForm):
     class Meta:
         model=Used
         fields='__all__'