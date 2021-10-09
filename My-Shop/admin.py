from django.contrib import admin
from django.db import models
from django.db.models import query
from .models import Product,Orders



#Altering admin site
admin.site.site_header = "MEMEZON"

class ProductAdmin(admin.ModelAdmin):

    @admin.action(description='Change to default category')
    def change_category(self, request, queryset):
        queryset.update(Category = "Default")

    @admin.action(description="Change to Out of stock")
    def outofstock(self, request, queryset):
        queryset.update(Instock = False)
    
    list_display = ('prod_name','prod_price','Category','Instock')
    search_fields = ['prod_name']
    actions = [change_category,outofstock,]
    fields = ['prod_price','prod_name']
    list_editable = ['prod_price']

    list_filter = ['Category']


# Register your models here
admin.site.register(Product, ProductAdmin)
admin.site.register(Orders)