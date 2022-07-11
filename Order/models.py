from tkinter import CASCADE
from django.db import models
from products.models import Product,Product_Seller,Colour,Varient
# Create your models here.
# import random
# from CustomUser.models import CustomUser

import datetime

PAYMENT_CHOICES = (
    ('Pay On Delivery','Pay On Delivery'),
    ('Card','Card'),
    ('Online Payment','Online Payment'),
)

class Products(models.Model):
    Item = models.ForeignKey(Product, on_delete=models.CASCADE)
    Seller = models.ForeignKey(Product_Seller, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    # Colour = models.ForeignKey(Colour, on_delete=models.CASCADE,blank=True)
    def __str__(self):
            return self.Item.Name


class Order(models.Model):
    netPrice = models.DecimalField(decimal_places=2, max_digits= 20)
    customer = models.ForeignKey("CustomUser.CustomUser",on_delete=models.CASCADE,blank=True,null=True)
    products = models.ManyToManyField(Products,blank=True,null=True)
    ordDate = models.DateTimeField(blank=True,auto_now = True)
    # paymentMode = models.CharField(
    #     max_length = 20,
    #     choices = PAYMENT_CHOICES,
    #     default = 'Pay On Delivery'
    #     )
    TransactionId = models.TextField(null=True,blank=True)
    Status = models.BooleanField(default=False)
    is_cart = models.BooleanField(default=True)
