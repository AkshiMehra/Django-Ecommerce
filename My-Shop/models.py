from django.db import models

# Create your models here.


class Product(models.Model):
    prod_name = models.CharField(max_length=500)
    prod_price = models.FloatField()
    discounted_price = models.FloatField()
    Category = models.CharField(max_length=500)
    Description = models.TextField()
    prod_img = models.CharField(max_length=10000)
    Instock = models.BooleanField(True)

    link = models.CharField(default="Link", max_length=100)

    def __str__(self):
        return self.prod_name

class Orders(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.name