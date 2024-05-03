from django.db import models
from django.contrib.auth .models import User
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.
class Categorystay(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name
    
class Sitterreg(models.Model):
    Sitter_name = models.CharField(max_length=30, null='False',blank = 'False')
    Sitter_number = models.CharField(max_length=30, null='False',blank = 'False')
    Date_of_birth = models.DateField(null="True", blank="True")
    Contact = models.IntegerField()
    Location = models.CharField(choices=[('kabalagala', 'kabalagala')], max_length=100)
    Gender =  models.CharField(choices=[('male', 'Male'),('female', 'Female')], max_length=100)
    Level_of_education = models.CharField(choices=[('Degree','Degree'),('Diploma','Diploma'),('Certificate','Certificate')],max_length=200,default=0)
    Next_of_kin = models.CharField(max_length=30, null='False',blank = 'False')
    NIN = models.CharField(max_length=30, null='False',blank = 'False')
    Recommenders_name = models.CharField(max_length=30, null='False',blank = 'False')
    Religion = models.CharField(max_length=30, null='True',blank = 'True')
    def __str__(self):
        return self.Sitter_name

class Sitter_arrival(models.Model):
    sitter_name=models.ForeignKey(Sitterreg, on_delete=models.CASCADE) 
    sitter_number=models.IntegerField(default=0)
    date_of_arrival=models.DateField(default=timezone.now)   
    timein=models.TimeField ()
    Attendancestatus = models.CharField(choices=[('onduty', 'On Duty'), ('offduty', 'Off Duty')], max_length=100)
    def __str__(self):
        return self.sitter_name
        
class Babyreg(models.Model):
    c_stay = models.ForeignKey(Categorystay,on_delete = models.CASCADE,null=False,blank = False)#this links class Babe to class Categorystay
    Baby_name = models.CharField(max_length=30, null='False',blank = 'False')
    Baby_number = models.CharField(max_length=30, null='False',blank = 'False')
    Date = models.DateField(default=timezone.now)
    Gender = models.CharField(max_length=30, null='False',blank = 'False')
    Age = models.IntegerField()
    Location = models.CharField(max_length=30, null='False',blank = 'False')
    Parents_names = models.CharField(max_length=30, null='False',blank = 'False')
    def __str__(self):
        return self.Baby_name

#Dolls    
class Category_doll(models.Model):  
     name = models.CharField(max_length=100,null=True, blank=True)
     def __str__(self):
         return self.name 
       
class Doll(models.Model):
    c_doll=models.ForeignKey(Category_doll, on_delete=models.CASCADE,null=True, blank=True)
    name_of_the_doll =models.CharField(max_length=200,null=True, blank=True)
    doll_number = models.CharField(max_length=200,null=True, blank=True)
    quantity=models.IntegerField(default=0)
    issued_quantity=models.IntegerField(default=0,blank=True,null=True) 
    received_quantity=models.IntegerField(default=0,null=True,blank=True)
    Unit_price=models.IntegerField(default=0,null=True, blank=True)
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name_of_the_doll
    
class Salesrecord(models.Model):    
    doll=models.ForeignKey(Doll, on_delete=models.CASCADE,null=False, blank=False)
    payee=models.ForeignKey(Babyreg, on_delete=models.CASCADE,null=False,blank=False)
    quantity_sold=models.IntegerField(default=0)
    amount_received=models.IntegerField(default=0)
    sale_date=models.DateField(default=timezone.now)
    unit_price=models.IntegerField(default=0)

    def __int__(self):
        return self.payee

    def get_total(self):
        total= self.quantity_sold * self.unit_price
        return int( total)
#here we are getting change.(money to be given to the parent)    
    def get_change(self):
        change= self.get_total() - self.amount_received
        return int(change)#sales is linked to products
    
    
#Procurement
class Category(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True) 
    def __str__(self):
        return self.name 
    
class Procurement(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)
    item_name = models.CharField(max_length=200,)
    Quantity=models.IntegerField(default=0)
    date=models.DateField(auto_now_add=True, null=True)
    Unit_price=models.IntegerField( null=True)
    received_quantity=models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.item_name
      
class Used(models.Model): 
    item = models.ForeignKey(Procurement,on_delete=models.CASCADE) 
    quantity_issued=models.IntegerField(default=0)
    usage_date=models.DateField()

#Baby arrival and departure
class Arrival(models.Model):
    baby_name=models.ForeignKey(Babyreg, on_delete=models.CASCADE)
    baby_number=models.CharField(max_length=30, null='False',blank = 'False')
    assign = models.ForeignKey(Sitterreg, on_delete = models.CASCADE,null=True,blank = True)
    date=models.DateField(default=timezone.now)
    timein=models.TimeField()
    broughtby=models.CharField(max_length=200)

    def __str__(self):
        return self.baby_number


class Departure(models.Model):
    baby_name=models.ForeignKey(Babyreg,on_delete=models.CASCADE)
    baby_number=models.CharField(max_length=10) 
    date=models.DateField(default=timezone.now)
    timeout=models.TimeField()
    picker=models.CharField(max_length=200)
    comment=models.CharField(max_length=200,null=True, blank=True)
    def __str__(self):
        return self.baby_name
    
#Babies payments
class Payment(models.Model):
    payee = models.ForeignKey(Babyreg,on_delete=models.CASCADE ,null=True, blank=True)
    c_payment = models.ForeignKey(Categorystay, on_delete=models.CASCADE,null=True, blank=True) 
    payno = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True)
    amount=models.IntegerField(null=False, blank=False)
    balance=models.IntegerField(null=True, blank=True)
    def __str__(self):
      return str(self.payee ) 
    
    def get_balance(self):
        return self.actual_amount - self.amount_paid  


#Sitter payments    
class Sitterpayment(models.Model):
    sitter_name = models.ForeignKey(Sitterreg, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)
    babies_assigned = models.IntegerField(default=0)

    def __str__(self):
        return f"Sitter Payment - {self.sitter_name}"

    def total_amount(self):
        total = self.amount * self.babies_assigned
        return total  # Removed int() conversion here

    