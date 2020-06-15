from django.db import models

# Create your models here.
class Product(models.Model): #product_category
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)

    history       = models.CharField(max_length=200)
    harmonizacao  = models.CharField(max_length=120)
    premios       = models.CharField(max_length=120)
