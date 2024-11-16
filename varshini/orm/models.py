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