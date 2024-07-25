from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.CharField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photo/categories', blank=True)
    list = [('mobile' , 'mobile'),
            ('computer' , 'computer'),
            ('sounds' , 'sounds'),
            ('routers' , 'routers'),
            ('cloths' , 'cloths')
    ]
    category = models.CharField(max_length=40 , null=True, blank=True, choices=list)


    def get_url(self):
        return reverse("product_by_category" , args=[self.slug])
    
    
    # to change the name of class which appear in the admin page
    class Meta:
        verbose_name="category"
        verbose_name_plural='categories'

    # to change the name of object with class field name or description field of class  

    def __str__(self):
        return self.category_name
