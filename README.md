# Ex02 Django ORM Web Application
## Date: 12.11.2024

## AIM
To develop a Django application to store and retrieve data from a Bank database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2024-11-18 141630.png>)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 customers.

## PROGRAM
```
admin.py

from django.contrib import admin
from.models import Loan,LoanAdmin
admin.site.register(Loan,LoanAdmin)

models.py

from django.db import models

# Create your models here.
from django.contrib import admin
class Loan(models.Model):
   loan_id=models.IntegerField(primary_key=True)
   loan_type=models.CharField(max_length=30)
   loan_amount=models.FloatField()
   cust_acntno=models.IntegerField()
   cust_name=models.CharField(max_length=50)

class LoanAdmin(admin.ModelAdmin):
    list_display=('loan_id','loan_type','loan_amount','cust_acntno','cust_name')
```

## OUTPUT
![alt text](<Screenshot 2024-11-16 140043.png>)
![alt text](<Screenshot 2024-11-18 140000-1.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
