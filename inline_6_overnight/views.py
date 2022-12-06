from django.shortcuts import render
from store.models import Order


def handler404(request, exception):
    """
    Django function-based view for the 404 error page
    """
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        # Create empty cart for now for non-logged in users
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}

    """ Error Handler 404 - Page Not Found """
    response = render(request, "errors/404.html", context=context)
    response.status_code = 404
    return response
