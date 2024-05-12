from django.db import models
from django.contrib.auth .models import User
from django.utils import timezone
from django.core.validators import MinValueValidator

#Create your models here.
class Sitterreg(models.Model):
    Sitter_name = models.CharField(max_length=30, null=False,blank=False)
    # Sitter_number = models.CharField(max_length=30, null=False,blank=False)
    Date_of_birth = models.DateField(null=True, blank=True)
    Contact = models.CharField(max_length=30,null=False,blank=False)
    date = models.DateTimeField()
    Location_choices = [('kabalagala', 'Kabalagala'),]
    Location = models.CharField(choices=Location_choices, max_length=100)
    Gender =  models.CharField(choices=[('male', 'Male'),('female', 'Female')], max_length=100)
    Level_of_education = models.CharField(choices=[('Degree','Degree'),('Diploma','Diploma'),('Certificate','Certificate')],max_length=200,default=0)
    Next_of_kin = models.CharField(max_length=30, null=False,blank=False)
    NIN = models.CharField(max_length=30, null=False,blank=False)
    Recommenders_name = models.CharField(max_length=30, null=False,blank=False)
    Religion = models.CharField(max_length=30, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return str(self.Sitter_name)


    
#Sitter payments    
class Sitterpayment(models.Model):
    # sitter_names = models.ForeignKey(Sitter_arrival, on_delete=models.CASCADE)
    amount = models.IntegerField(default=3000)
    date = models.DateField(default=timezone.now)
    babies_assigned = models.IntegerField(default=0)
    def __str__(self):
        return f"Sitter Payment - {self.sitter_names.sitter_name}"

    def total_amount(self):
        total = self.amount * self.babies_assigned
        return total  # Removed int() conversion here



 #Babies 
class Categorystay(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return str(self.name) 
    

         
class Babyreg(models.Model):
    Baby_name = models.CharField(max_length=30, null=False, blank=False)
    fathers_names = models.CharField(max_length=30, null=False, blank=False)
    mothers_names = models.CharField(max_length=30, null=False, blank=False)
    c_stay = models.ForeignKey(Categorystay, on_delete=models.SET_NULL, null=True, blank=True)
    # assigned = models.ForeignKey(Sitter_arrival, on_delete=models.SET_NULL, null=True, blank=True)
    Date = models.DateTimeField()
    Gender = models.CharField(max_length=30, null=False, blank=False)
    Age = models.IntegerField()
    Location = models.CharField(max_length=30, null=False, blank=False)
    brought = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        print(f"Baby name: {self.Baby_name}, Type: {type(self.Baby_name)}")
        if self.Baby_name is not None:
            return str(self.Baby_name)
        else:
            return "Unnamed Baby"

#sitter arrival
class Sitter_arrival(models.Model):
    sitter_name=models.ForeignKey(Sitterreg, on_delete=models.CASCADE) 
    date_of_arrival=models.DateTimeField()  
    # timein=models.TimeField ()
    # timeout=models.TimeField (null=True, blank=True)
    # Attendancestatus = models.CharField(choices=[('onduty', 'On Duty'), ('offduty', 'Off Duty')], max_length=100)
    Attendancestatus = models.BooleanField(default=False)
    babies = models.ManyToManyField(Babyreg)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.sitter_name.Sitter_name
    

#Babies departure      
class Departure(models.Model):
    baby_name=models.ForeignKey(Babyreg,on_delete=models.CASCADE) 
    date=models.DateTimeField() 
    # timeout=models.TimeField()
    picker=models.CharField(max_length=200)
    contact = models.CharField(max_length=30)
    NIN = models.CharField(max_length=30, null='False',blank = 'False')
    comment=models.CharField(max_length=200,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return str(self.baby_name)
    
#Babies payments
class Categorymode(models.Model):
    c_name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return str(self.c_name)



class Payment(models.Model):
    payee = models.ForeignKey(Babyreg, on_delete=models.CASCADE, null=True, blank=True)
    c_payment = models.ForeignKey(Categorystay, on_delete=models.SET_NULL, null=True, blank=True)
    c_mode = models.ForeignKey(Categorymode, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    amount_choices = [
        (10000, '10,000'),
        (15000, '15,000'),
        (300000, '300,000'),
        (450000, '450,000'),
    ]
    selected_amount = models.IntegerField(choices=amount_choices, null=False, blank=False,default=0)
    amount_paid = models.IntegerField(null=False, blank=False)
    payment_status = models.CharField(choices=[('Cleared', 'Cleared'), ('Pending', 'Pending')], max_length=100,default=0)
    balance = models.IntegerField(null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        self.balance = self.selected_amount - self.amount_paid
        super().save(*args, **kwargs)
        

    def __str__(self):
        return str(self.payee)


#Dolls    
class Category_doll(models.Model):  
     name = models.CharField(max_length=100,null=True, blank=True)
     def __str__(self):
         return str(self.name)
       
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
    payee = models.ForeignKey(Babyreg, on_delete=models.SET_NULL, null=True, blank=True)
    quantity_sold=models.IntegerField(default=0)
    amount_received=models.IntegerField(default=0)
    sale_date=models.DateField(default=timezone.now)
    unit_price=models.IntegerField(default=0)

    def __str__(self):
        return str(self.payee)

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
        return str(self.name) 
    
class Procurement(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    item_name = models.CharField(max_length=200)
    Quantity = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True, null=True)
    Unit_price = models.IntegerField(null=True)
    received_quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.item_name)

    # def total_amount(self):
    #     if self.Quantity is not None and self.Unit_price is not None:
    #         return self.Quantity * self.Unit_price
    #     return 0

class Used(models.Model):
    item = models.ForeignKey(Procurement, on_delete=models.CASCADE)
    quantity_issued = models.IntegerField(default=0)
    issue_date = models.DateField(default=timezone.now)
    issued_to = models.CharField(default=0, max_length=100)

    def __str__(self):
        return f"Issued {self.quantity_issued} units of {self.item.item_name} on {self.issue_date}"








    