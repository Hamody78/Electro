from django.shortcuts import render, get_object_or_404
from Categories.models import Category
from .models import Product
from carts.views import _cart_id
from carts.models import *

# Create your views here.

def store(request, total=0, category_slug=None):
    cart_items = Cartitem.objects.filter(cart__cart_id=_cart_id(request), is_active=True)
    cart_items_count = cart_items.count()
    all_products = Product.objects.all()
    psad = []
    for q in all_products:
        psad.append(q.price_after_discount)
    psad.sort()

    # Top selling filter
    topselles = []
    
    for y in all_products:
        if y.brand == True:
            count_selles = y.number_sells
            topselles.append(count_selles)
        else:
            continue

    topselles.sort()
    top = topselles[::-1]
    topselles_pro = []

    for t in range(0,3):
        pro1 = get_object_or_404(Product, number_sells=top[t])
        topselles_pro.append(pro1)


    # Category Filter
    category = None
    products = None
    categories = Category.objects.all()
    brands = Product.objects.all().filter(brand=True)

    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        product_count = products.count()
     
    else:
        products = Product.objects.all()
        product_count = products.count()

    # price filter
    ap = []
    min_number = request.GET.get("min_number")
    max_number = request.GET.get("max_number")

    for product in products:
        ap.append(product)

    price_list = []
    for p in ap:
        if min_number != None and max_number != None:
            if p.price_after_discount >= float(min_number) and p.price_after_discount <= float(max_number):
                price_list.append(p)

    count_price_list = len(price_list)

    for cart_item in cart_items:
        total += (cart_item.product.price_after_discount * cart_item.quantity)

    context = {
        'cat' : categories, 
        'pro' : ap, 
        'brand' : brands,
        'procount' : product_count,
        'topSellingProduct' : topselles_pro,
        'price_list' : price_list,
        "count_price_list":count_price_list,
        "cart_items_count":cart_items_count,
        "last_product":int(psad[len(psad)-1])+1,
        "min_number":min_number,
        "max_number":max_number,
        "cart_items":cart_items,
        "total":total,
    }

    return render(request, 'store.html' , context)


# configure the single product page
def product_details(request, category_slug, product_slug, total=0):
    cart_items = Cartitem.objects.filter(cart__cart_id=_cart_id(request), is_active=True)
    cart_items_count = cart_items.count()
    for cart_item in cart_items:
        total += (cart_item.product.price_after_discount * cart_item.quantity)
    categories = Category.objects.all()
    try:
        single_product = Product.objects.get(category__slug=category_slug , slug=product_slug)
        related_products = Product.objects.filter(category__category_name=single_product.category.category_name)
    except Exception:
        raise Exception
    
    
    context = {
        'cat' : categories, 
        'single_product' : single_product,
        "cart_items_count":cart_items_count,
        "pro":related_products,
        "cart_items":cart_items,
        "total":total,
    }

    return render(request, 'product_details.html', context)