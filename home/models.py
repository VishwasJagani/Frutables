from django.db import models

# Create your models here.

class register(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    image = models.FileField(default="",upload_to="user/")

    def __str__(self) -> str:
        return f'{self.fname} {self.lname}'
