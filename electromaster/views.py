from django.shortcuts import render
from Categories.models import Category # this is related to context
from store.models import Product
from django.shortcuts import get_object_or_404
from carts.views import _cart_id
from carts.models import *


def home(request, total=0, category_slug=None):
    category= Category.objects.all()
    products= Product.objects.all()
    brands= Product.objects.all().filter(brand=True)
    all_products = Product.objects.all()
    topselles = []
    cart_items = Cartitem.objects.filter(cart__cart_id=_cart_id(request), is_active=True)
    cart_items_count = cart_items.count()

    for cart_item in cart_items:
        total += (cart_item.product.price_after_discount * cart_item.quantity)

    
    for y in all_products:
        count_selles = y.number_sells
        topselles.append(count_selles)

    topselles.sort()
    top = topselles[::-1]
    topselles_pro = []

    for t in range(0,3):
        pro1 = get_object_or_404(Product, number_sells=top[t])
        topselles_pro.append(pro1)

    context = {
        'cat' : Category.objects.all(), 
        'pro' : products, 
        'brand' : brands,
        'topSellingProduct' : topselles_pro,
        "cart_items_count":cart_items_count,
        "cart_items":cart_items,
        "total":total,
    }
    return render(request , 'index.html', context)

def track(request):
    return render(request, "pages/track.html")

def contact(request):
    return render(request, "pages/contact.html")

def privacy_policy(request):
    return render(request, "pages/privacy.html")

def about(request):
    return render(request, "pages/about.html")

def terms_conditions(request):
    return render(request, "pages/terms.html")

def payment_methods(request):
    return render(request, "pages/customer_payment.html")

def refunds_returns_policy(request):
    return render(request, "pages/returns_policy.html")

def shipping_delivery(request):
    return render(request, "pages/shipping.html")

def frequently_asked_questions(request):
    return render(request, "pages/questions.html")

def wishlist(request):
    return render(request, "wishlist.html")

def compare(request):
    return render(request, "compare.html")
