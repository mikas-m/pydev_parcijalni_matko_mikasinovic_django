from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    vat_id = models.IntegerField(len=11)
    street = models.TextField()
    city = models.TextField()
    country = models.TextField()
    