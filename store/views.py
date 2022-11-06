from django.shortcuts import render
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
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    """
    Django function-based view for the checkout page
    """
    context = {}
    return render(request, 'store/checkout.html', context)
