from django.contrib import admin
from . models import Carts
from . models import Cartitem
# Register your models here.
admin.site.register(Carts)
admin.site.register(Cartitem)
