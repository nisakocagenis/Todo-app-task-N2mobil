from django.db import models 
from django.contrib.auth.models import AbstractUser



class Address(models.Model):
    street = models.CharField(max_length=50)
    suite = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField(null=True)

class Company(models.Model):
    name = models.CharField(max_length=120)

class User(AbstractUser): 
    location = models.CharField(max_length=255, blank=True) 
    website = models.URLField(max_length=255, blank=True) 
    phone_no = models.CharField(max_length=10)
    address = models.ForeignKey(Address, on_delete=models.CASCADE ,related_name="users" , null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(null=True, upload_to='static/korall/')






