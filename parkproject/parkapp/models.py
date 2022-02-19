from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TYPER(models.Model):
    status_choices = [
        ('O','owner'),
        ('C','customer')
    ]
    usertype =  models.CharField(max_length = 2,choices=status_choices)
    user =  models.CharField(max_length=50)

class OWNER(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    no_of_slots = models.IntegerField()
    # prices= models.IntegerField()######changes

class CUSTOMER(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)


class BOOK(models.Model):
    owner = models.CharField(max_length=30)
    customer = models.CharField(max_length=30)
    key_num = models.IntegerField()
    date = models.DateField(error_messages={'required': "This field is required."})
    time = models.TimeField(error_messages={'required': "This field is required."})
    bool_value = models.BooleanField(default=False)
    spot = models.CharField(max_length=50)

