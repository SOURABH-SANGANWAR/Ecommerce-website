from unicodedata import category
from django.db import models
from django.utils.html import mark_safe
# from CustomUser.models import CustomUser
from django.urls import reverse

# Create your models here.

# Categories = (
#     ('Electronics','Electronics'),
#     ('Groceries','Groceries'),
#     ('Eatbles','Eatbles'),
#     ('Unknown','Unknown'),
# )


def Product_img(instance,filename):
    return 'Img/Products/product_/{0}/{1}'.format(instance.Name[:10],filename)

def Category_img(instance,filename):
    return 'Img/Categories/{0}/{1}'.format(instance.Name[:10],filename)

class Varient(models.Model):
    Name = models.TextField(max_length=50, unique=True)
    def __str__(self):
        return self.Name 

class SuperCategory(models.Model):
    Name = models.TextField(max_length=50, unique=True)
    def __str__(self):
        return self.Name

class Category(models.Model):
    Name = models.TextField(max_length=50, unique=True)
    Cat = models.ForeignKey(SuperCategory,blank=True,null=True,on_delete=models.CASCADE)
    Image = models.ImageField(default='Img/default_prduct.jpg', upload_to=Category_img)
    def get_view_url(self):
        return reverse("Products:detail_view_filter",kwargs={'id': self.id})
    def __str__(self):
        return self.Name
        

class Colour(models.Model):
    Name = models.TextField(max_length=50, unique=True)
    def __str__(self):
        return self.Name

class Review(models.Model):
    Name = models.TextField()
    desc = models.TextField()
    Title = models.TextField(blank=True, null=True)
    Rating = models.IntegerField()
    def __str__(self):
        return self.Name

class Product_Seller(models.Model):
    Name = models.ForeignKey('CustomUser.CustomUser', on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=20,decimal_places=2)
    def __str__(self):
        return self.Name.username
    def HTMLaddr(self):
        if(self.Name.city!= None):
            # return "<h5 style = 'display: inline-block;'>Seller : "+self.Name.username+"</h5><span>&nbsp;&nbsp;&nbsp;("+self.Name.city.cityName+", "+self.Name.country+")</span>"
            return "<h5 style = 'display: inline-block;'>Seller : "+self.Name.username+"</h5><span>&nbsp;&nbsp;&nbsp;("+self.Name.city+", "+self.Name.country+")</span>"
        return "<h5 style = 'display: inline-block;'>Seller : "+self.Name.username+"</h5><span>&nbsp;&nbsp;&nbsp;(" +self.Name.country+")</span>"


class Product(models.Model):
    Name = models.TextField()
    Image = models.ImageField(default='Img/default_prduct.jpg', upload_to=Product_img)
    Price = models.DecimalField(decimal_places=2, max_digits=20)
    MRP = models.DecimalField(decimal_places=2, max_digits=20)
    Varients = models.ForeignKey(Varient,blank=True,null =True, on_delete=models.CASCADE)
    Colours = models.ManyToManyField(Colour,blank=True)
    Sellers = models.ManyToManyField(Product_Seller,null=True,blank=True)
    Reviews = models.ManyToManyField(Review,blank=True)
    Rating = models.DecimalField(decimal_places=1,max_digits=2,null=True)
    description = models.TextField(blank=True, null=True, default='Will be updated Soon')
    features = models.TextField(blank=True, null=True, default='Will be updated Soon')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    varient_desc = models.TextField(blank=True,null=True)
    Product_tags = models.TextField(default=Name)
    is_offer = models.BooleanField(default=False)
    is_best = models.BooleanField(default=False)
    is_root = models.BooleanField(default=True)
    def Image_tag(self):
            return mark_safe('<img src="/media/%s" width="150" height="150" style = "border-radius : 75px;"/>' % (self.Image))
    
    def get_view_url(self):
        return reverse("Products:detail_view",kwargs={'id':self.id})
    def update_url(self):
        return reverse("products:update_view",kwargs={'id':self.id})
    def __str__(self):
        return self.Name




class Offers(models.Model):
    Product_list = models.ManyToManyField(Product,blank=True)

class BestSellers(models.Model):
    Product_list = models.ManyToManyField(Product,blank=True)