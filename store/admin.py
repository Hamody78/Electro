from django.contrib import admin
from .models import *

# to automatically fill the slug field

class Product_Admin(admin.ModelAdmin): 
    prepopulated_fields = {"slug":("product_name",)}
    # to make a new list in the admin category page ( category_name    slug )
    list_display=('id', 'product_name' , 'slug' , 'price' , 'stock' , 'category' ,'is_available', 'created_date', 'modified')


class Variation_Admin(admin.ModelAdmin): 
    list_display=('id', "variation_category", "variation_value", 'is_active')
    list_display_links = ("id",)
    list_editable = ("is_active",)


admin.site.register(Product, Product_Admin)
admin.site.register(Variation)