"""
products models
"""
from django.db import models
from stores.models import Store


class Product(models.Model):
    """
    product model
    """
    name = models.CharField(max_length=50)
    desription = models.TextField(max_length=1000)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    features = models.ManyToManyField(to="Feature")
    price = models.IntegerField(default=0)
    negotiable = models.BooleanField(default=False)


class Image(models.Model):
    """
    product image model
    """
    image = models.ImageField(upload_to="products/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Feature(models.Model):
    """
    product feature model
    """
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)