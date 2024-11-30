from django.db import models
import random

# Create your models here.

class register(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    number = models.IntegerField()
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    image = models.FileField(default="",upload_to="user/")
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.IntegerField()
    token = models.IntegerField(default=random.randint(1111,9999))

    def __str__(self):
        return f'{self.fname} {self.lname}'
    
class slider(models.Model):
    name = models.CharField(max_length=10)
    image = models.FileField(upload_to="slider/")

    def __str__(self):
        return self.name
