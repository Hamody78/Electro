from django.db import models
from store.models import Product, Variation
# Create your models here.

class Carts(models.Model):
    cart_id      = models.CharField(max_length=350 , blank=True)
    date_added   = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
    # to change the name of class which appear in the admin page
    class Meta:
        verbose_name="Cart"
        verbose_name_plural='Carts'

class Cartitem(models.Model):
    product         = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations      = models.ManyToManyField(Variation, blank=True)
    cart            = models.ForeignKey(Carts, on_delete=models.CASCADE)
    quantity        = models.IntegerField()
    is_active       = models.BooleanField(default=True)

    def subtotal(self):
        return self.product.price_after_discount * self.quantity

    def __str__(self):
        return self.product.product_name

    # to change the name of class which appear in the admin page
    class Meta:
        verbose_name="Cart_item"
        verbose_name_plural='Cart items'

