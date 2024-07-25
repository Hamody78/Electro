from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('' , views.store , name='store'),
    path('<slug:category_slug>/' , views.store , name='product_by_category'),   # Category Filter
    path('<slug:category_slug>/<slug:product_slug>/' , views.product_details , name='product_by_details'),# configure the single product page
]
