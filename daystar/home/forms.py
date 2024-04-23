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



