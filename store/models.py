from django.db import models
from Categories.models import Category
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    product_name              = models.CharField(max_length=50 , unique=True)
    slug                      = models.SlugField(max_length=50)
    short_description         = models.TextField(max_length=500, null=True, blank=True)
    long_description          = models.TextField(max_length=10000, null=True, blank=True)
    price                     = models.FloatField(default=0)
    price_after_discount      = models.FloatField(default=0)
    image                     = models.ImageField(upload_to= 'photo/products')
    image1                    = models.ImageField(upload_to= 'photo/products', default="img.jpg", null=True, blank=True)
    image2                    = models.ImageField(upload_to= 'photo/products', default="img.jpg", null=True, blank=True)
    image3                    = models.ImageField(upload_to= 'photo/products', default="img.jpg", null=True, blank=True)
    image4                    = models.ImageField(upload_to= 'photo/products', default="img.jpg", null=True, blank=True)
    # Description
    image5                    = models.ImageField(upload_to= 'photo/products', default="img.jpg", null=True, blank=True)
    image6                    = models.ImageField(upload_to= 'photo/products', default="img.jpg", null=True, blank=True)
    image7                    = models.ImageField(upload_to= 'photo/products', default="img.jpg", null=True, blank=True)
    image8                    = models.ImageField(upload_to= 'photo/products', default="img.jpg", null=True, blank=True)

    stock                     = models.IntegerField()
    brand                     = models.BooleanField(default=True)
    number_sells              = models.IntegerField(default=0)       
    is_available              = models.BooleanField(default=True)
    category                  = models.ForeignKey(Category, on_delete=models.CASCADE )
    created_date              = models.DateTimeField(auto_now_add=True)
    modified                  = models.DateTimeField(auto_now=True)


    def get_url(self):
        return reverse("product_by_details" , args=[self.category.slug , self.slug])




    # to change the name of class which appear in the admin page
    class Meta:
        verbose_name="product"
        verbose_name_plural='products'

    # to change the name of object with class field name or description field of class  

    def __str__(self):
        return self.product_name
    

variation_categories_choisis = [
    ("model", "model"),
    ("color", "color"),
]

class VariatonManager(models.Manager):
    def modelss(self):
        return super(VariatonManager, self).filter(variation_category="model", is_active=True)
    def colors(self):
        return super(VariatonManager, self).filter(variation_category="color", is_active=True)

class Variation(models.Model):
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_categories_choisis)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariatonManager()


    def __str__(self):
        return self.variation_value
