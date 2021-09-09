from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200,null=True)
    product_price = models.CharField(max_length=200,null=True)

