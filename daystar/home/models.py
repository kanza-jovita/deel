
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
    c_stay = models.ForeignKey(Categorystay,on_delete = models.CASCADE,null=True,blank = True)#this links class Babe to class Categorystay
    assign = models.ForeignKey(Sitterreg, on_delete = models.CASCADE,null=True,blank = True)
    Baby_name = models.CharField(max_length=30, null='False',blank = 'False')
    Baby_number = models.CharField(max_length=30, null='False',blank = 'False')
    Date = models.DateField(max_length=30, null='False',blank = 'False')
    Gender = models.CharField(max_length=30, null='False',blank = 'False')
    Age = models.IntegerField()
    Location = models.CharField(max_length=30, null='False',blank = 'False')
    Name_of_person_who_brought_the_baby =  models.CharField(max_length=30,null="False",blank = "False")
    Name_of_the_person_that_has_taken_baby =  models.CharField(max_length=30,null="False",blank = "False")
    Time_In = models.TimeField(max_length=30, null='False',blank = 'False')
    Time_Out = models.TimeField(max_length=30, null='False',blank = 'False')
    Parents_names = models.CharField(max_length=30, null='False',blank = 'False')
    Comment = models.CharField(max_length=100, null='False',blank = 'False')
    def __str__(self):
        return self.Baby_name
    

class Payment(models.Model):
    payee = models.ForeignKey(Babyreg,on_delete = models.CASCADE,null=True,blank = True)
    c_pay = models.ForeignKey(Categorystay,on_delete = models.CASCADE,null=True,blank = True)
    pay_no = models.IntegerField(null=True,blank=True)
    Amount = models.IntegerField(null=True,blank=True)
    currency = models.CharField(default='Ugx',null=True,blank=True ,max_length=5)

    

class Doll (models.Model):
    baby_name= models.ForeignKey(Babyreg,on_delete = models.CASCADE,null=True,blank = True)
    doll_name = models.CharField(max_length=100,null='False', blank = 'False')
    number = models.IntegerField(null='False', blank = 'False')
    price = models.IntegerField(null='False', blank = 'False')
    

    def __str__(self):
        return self.doll_name

class Category(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False,unique=True)
    def __str__(self):
        return self.name
# defining a model for product
class Product(models.Model):
    Category_name=models.ForeignKey(Category, on_delete=models.CASCADE,null=False,blank=False)
    product_name=models.CharField(max_length=50,null=False,blank=False)
    total_quantity=models.IntegerField(default=0,null=False,blank=False,validators=[MinValueValidator(1)])
    received_quantity=models.IntegerField(default=0,null=False,blank=False)
    issued_quantity=models.IntegerField(default=0,null=False,blank=False)
    unit_price=models.IntegerField(default=0,null=False,blank=False)


    
