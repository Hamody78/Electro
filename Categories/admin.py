from django.contrib import admin
from .models import Category

# to automatically fill the slug field

class Category_Admin(admin.ModelAdmin): 
    prepopulated_fields = {"slug":("category_name",)}
    # to make a new list in the admin category page ( category_name    slug )
    list_display=('category_name' , 'slug')
# Register your models here.

admin.site.register(Category, Category_Admin)
