from django.db import models
import random

# Create your models here.

#This Models is For User to create account
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
    
#This Models is for Slider   
class slider(models.Model):
    name = models.CharField(max_length=10)
    image = models.FileField(upload_to="slider/")

    def __str__(self):
        return self.name

#This Models Is For Displaying Information About Company
class Contact(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.IntegerField()
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class subcategory(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class product(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField(max_length=100)
    price = models.IntegerField()
    origin = models.CharField(max_length=100)
    weight = models.CharField(max_length=10)
    image = models.FileField(upload_to="product/")
    cat = models.ForeignKey(category , on_delete=models.CASCADE)
    quality = models.ForeignKey(subcategory , on_delete=models.CASCADE)

    def __str__(self):
        return self.name