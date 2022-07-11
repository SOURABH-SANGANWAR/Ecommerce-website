from django.contrib import admin

# Register your models here.

from .models import Order,Products

# admin.site.register(Order)

admin.site.register(Products)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("TransactionId", "netPrice")#, "paymentMode"
    search_fields = ('TransactionId',)

