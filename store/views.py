from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def store(request):
    """
    Django function-based view for the store (or home) page
    """
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):
    """
    Django function-based view for the cart page
    """
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        # Create empty cart for now for non-logged in users
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    """
    Django function-based view for the checkout page
    """
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        # Create empty cart for now for non-logged in users
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    """
    Django function-based view to create/add quantity to an OrderItem
    or remove/delete the item if the action sent over is 'remove'
    """
    return JsonResponse('Item was added', safe=False)
