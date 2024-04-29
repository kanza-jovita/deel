
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
    Location = models.CharField(max_length=30, null='False',blank = 'False')
    Gender =  models.CharField(max_length=10,null="False",blank = "False")
    Level_of_education = models.CharField(max_length=30, null='False',blank = 'False')
    Next_of_kin = models.CharField(max_length=30, null='False',blank = 'False')
    NIN = models.CharField(max_length=30, null='False',blank = 'False')
    Recommenders_name = models.CharField(max_length=30, null='False',blank = 'False')
    Religion = models.CharField(max_length=30, null='True',blank = 'True')
    def __str__(self):
        return self.Sitter_name

     
    
class Babyreg(models.Model):
    c_stay = models.ForeignKey(Categorystay,on_delete = models.CASCADE,null=False,blank = False)#this links class Babe to class Categorystay
    assign = models.ForeignKey(Sitterreg, on_delete = models.CASCADE,null=True,blank = True)
    Baby_name = models.CharField(max_length=30, null='False',blank = 'False')
    Baby_number = models.CharField(max_length=30, null='False',blank = 'False')
    Date = models.DateField(max_length=30, null='False',blank = 'False')
    Gender = models.CharField(max_length=30, null='False',blank = 'False')
    Age = models.IntegerField()
    Location = models.CharField(max_length=30, null='False',blank = 'False')
    Parents_names = models.CharField(max_length=30, null='False',blank = 'False')
    def __str__(self):
        return self.Baby_name
    

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

     
  
    def get_total(self):
        total= self.quantity_sold * self.unit_price
        return int( total)
#here we are getting change.(money to be given to theparent)    
    def get_change(self):
        change= self.get_total() - self.amount_received
        return int(change)#sales is linked to products
    


#models for arrival and departure

class Arrival(models.Model):
    baby_name=models.ForeignKey(Babyreg, on_delete=models.CASCADE)
    baby_number=models.IntegerField(default=0)
    date=models.DateField(default=timezone.now)
    timein=models.TimeField()
    care_giver=models.CharField(max_length=200)
    amount=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.baby_number


class Departure(models.Model):
    baby_name=models.ForeignKey(Babyreg,on_delete=models.CASCADE)
    baby_number=models.IntegerField(default=0) 
    date=models.DateField(default=timezone.now)
    timeout=models.TimeField()
    picker=models.CharField(max_length=200)
    comment=models.CharField(max_length=200,null=True, blank=True)
    def __str__(self):
        return self.baby_name
    

#Payment model
