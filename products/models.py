from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=2083, null=True)
    price = models.FloatField()
    stock = models.FloatField()
    discount = models.FloatField()
    image_url = models.CharField(max_length=2083)
