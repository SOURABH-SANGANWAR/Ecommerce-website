from django.contrib import admin
from .models import Product,Varient,Colour,Category,Review,SuperCategory,Product_Seller,Offers,BestSellers

# Register your models here.
# admin.site.register(Product)
admin.site.register(Varient)
admin.site.register(Colour)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Product_Seller)
admin.site.register(SuperCategory)
admin.site.register(Offers)
admin.site.register(BestSellers)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("Name", "Price", "MRP", "category", "Image_tag")
    search_fields = ('Name', "category")
    # readonly_fields = ('get_view_url',)
