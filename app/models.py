from django.db import models

# Create your models here.
class InvestmentLoginModel(models.Model):
    name=models.CharField(max_length=100)
    emailid=models.EmailField()
    mobile_no=models.CharField(max_length=10)