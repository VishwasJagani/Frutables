from django.db import models
from home.models import *

# Create your models here.

class cart(models.Model):
    user_id = models.ForeignKey(register, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f"{self.user_id.fname}"    