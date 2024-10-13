from django.contrib import admin
from smallshop import models
# Register your models here.

@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['pId', 'pName', 'pDate', 'pCount','pCategory', 'pPhoto']

@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['cId', 'cName']

@admin.register(models.Shops)
class ShopsAdmin(admin.ModelAdmin):
    list_display = ['sId', 'sName']

@admin.register(models.Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['custId', 'custName']
