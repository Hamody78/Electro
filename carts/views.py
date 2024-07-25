from django.shortcuts import render, redirect
from store.models import Product, Variation
from carts.models import *

# Create your views here.

def _cart_id(   request   ): # Get Session id
    cart_session_id = request.session.session_key
    if not cart_session_id:
        cart_session_id = request.session.create()
    return cart_session_id


def add_cart(request, product_id): # 6
    # Product + Cart ==> CartItem
    # Product
    product = Product.objects.get(id=product_id)
    product_variation = []

    if request.method == "POST":
        for item in request.POST:
            key = item
            value = request.POST[key]

            try:
                variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                product_variation.append(variation)
            except:
                pass

    quantity = request.POST.get("quantity")
    print(quantity)

    # Cart
    try:
        cart = Carts.objects.get(cart_id=_cart_id(request))
    except Carts.DoesNotExist:
        cart = Carts.objects.create(
            cart_id=_cart_id(request),
        )
    cart.save()

    # CartItem
    is_cart_item_exists = Cartitem.objects.filter(cart=cart, product=product).exists()
    if is_cart_item_exists:
        cart_item = Cartitem.objects.filter(cart=cart, product=product)

        ex_var_list = []
        id = []
        for item in cart_item:
            existing_variation = item.variations.all()
            ex_var_list.append(list(existing_variation))
            id.append(item.id)

        if product_variation in ex_var_list:
            index = ex_var_list.index(product_variation) # 1
            item_id = id[index]


            item = Cartitem.objects.get(product=product, id=item_id)
            if quantity != None:
                item.quantity = item.quantity + int(quantity)
            else:
                item.quantity = item.quantity + 1            
            
            item.save()

        else:
            if quantity != None:
                item = Cartitem.objects.create(cart=cart, quantity=float(quantity), product=product)
            else:
                item = Cartitem.objects.create(cart=cart, quantity=1, product=product)
            if len(product_variation) > 0:
                item.variations.clear()
                item.variations.add(*product_variation)
            item.save()
    


    else:
        if quantity != None:
            cart_item = Cartitem.objects.create(cart=cart, quantity=int(quantity), product=product)
        else:
            cart_item = Cartitem.objects.create(cart=cart, quantity=1, product=product)
        if len(product_variation) > 0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variation)
        cart_item.save()

    return redirect("cart")

def remove_cart(request, product_id, core_id):
    # CartItem
    try:
        cart_item = Cartitem.objects.get(cart__cart_id=_cart_id(request), product__id=product_id, id=core_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect("cart")
    
def remove_cart_item(request, product_id, core_id):
    # CartItem
    cart_item = Cartitem.objects.get(cart__cart_id=_cart_id(request), product__id=product_id, id=core_id)
    cart_item.delete()
    return redirect("cart")

def cart(request, total=0, quantity=0, cart_items=None):

    cart_items = Cartitem.objects.filter(cart__cart_id=_cart_id(request), is_active=True)
    cart_items_count = cart_items.count()
    for cart_item in cart_items:
        total += (cart_item.product.price_after_discount * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (15 / 100) * total
    grand_total = tax + total

    if len(cart_items) == 0:
        empty = 0
    else:
        empty = 1

    context = {
        "cart_items":cart_items,
        "cart_items_count":quantity,
        "total":total,
        "tax":tax,
        "grand_total":grand_total,
        "empty":empty
    }
    return render(request, 'cart.html', context)