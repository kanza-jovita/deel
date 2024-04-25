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

class AddForm(ModelForm):
    class Meta:
        model=Product
        fields=['received_quantity'] # received stock for workers to edit(incoming stock)


class SaleForm(ModelForm):
    class Meta:
        model=Sale
        fields=['quantity', 'amount_received','issued_to', 'contact']

