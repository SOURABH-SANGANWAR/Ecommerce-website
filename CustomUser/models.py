from django.db import models
from django.utils.html import mark_safe
from .manager import *
# Create your models here.
from Order.models import Order

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe

def user_profile_dir(instance,filename):
    return 'profile_pics/user_/{0}/{1}'.format(instance.id,filename)

# class Product_Seller(models.Model):
#     Name = models.ForeignKey(models.CustomUser, on_delete=models.CASCADE)
#     Price = models.DecimalField(max_digits=20,decimal_places=2)
#     def __str__(self):
#         return self.Name.username
#     def HTMLaddr(self):
#         return "<h5 style = 'display: inline-block;'>Seller : "+self.Name.username+"</h5><span>&nbsp;&nbsp;&nbsp;("+self.Name.city+", "+self.Name.country+")</span>"
class City(models.Model):
    cityName = models.TextField(unique=True)
    def __str__(self):
        return self.cityName

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.TextField(null=True)
    phone_no = models.IntegerField(null=True)
    city = models.ForeignKey(City,blank=True,on_delete=models.CASCADE,null=True)
    country = models.TextField(blank=True,default='India')
    is_ph_verified = models.BooleanField(default=False)
    USERNAME_FIELD =  'email'
    is_deliveryAgent = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to=user_profile_dir)
    MyOrders = models.ManyToManyField(Order)
    address = models.TextField(blank=True)
    objects = UserManager()
    REQUIRED_FIELDS = []
    def __str__(self):
        return f'{self.username}'
    def image_tag(self):
            return mark_safe('<img src="/media/%s" width="150" height="150" style = "border-radius : 75px;"/>' % (self.image))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True