from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from accounts.decorators import customer_required
from products.models import Product
from .models import Order, OrderItem
from .forms import CheckoutForm
from .cart import Cart


# ===========================
# Cart
# ===========================

@customer_required
def cart(request):

    cart = Cart(request)

    items = list(cart)

    packaging_charge = Decimal("20.00")
    delivery_charge = Decimal("0.00")

    total = cart.get_total_price()

    grand_total = (
        total +
        packaging_charge +
        delivery_charge
    )

    return render(
        request,
        "orders/cart.html",
        {
            "items": items,
            "cart": cart,
            "total": total,
            "packaging_charge": packaging_charge,
            "delivery_charge": delivery_charge,
            "grand_total": grand_total,
        },
    )


# ===========================
# Add To Cart
# ===========================

@customer_required
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
        is_active=True,
    )

    cart = Cart(request)

    cart.add(product)

    messages.success(
        request,
        "Product added to cart successfully."
    )

    return redirect("cart")


# ===========================
# Remove From Cart
# ===========================

@customer_required
def remove_from_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
    )

    cart = Cart(request)

    cart.remove(product)

    messages.success(
        request,
        "Item removed from cart."
    )

    return redirect("cart")


# ===========================
# Increase Quantity
# ===========================

@customer_required
def increase_quantity(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
    )

    cart = Cart(request)

    cart.increase(product)

    return redirect("cart")


# ===========================
# Decrease Quantity
# ===========================

@customer_required
def decrease_quantity(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
    )

    cart = Cart(request)

    cart.decrease(product)

    return redirect("cart")
    
# ===========================
# Checkout
# ===========================

@customer_required
def checkout(request):

    cart = Cart(request)

    if len(cart) == 0:
        messages.error(request, "Your cart is empty.")
        return redirect("products")

    form = CheckoutForm()

    packaging_charge = Decimal("20.00")
    delivery_charge = Decimal("0.00")

    total = cart.get_total_price()
    grand_total = total + packaging_charge + delivery_charge

    if request.method == "POST":

        form = CheckoutForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)
            order.customer = request.user
            order.total = grand_total
            order.save()

            for item in cart:

                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    quantity=item["quantity"],
                    price=item["price"],
                )

            cart.clear()

            messages.success(
                request,
                "Your order has been placed successfully."
            )

            return redirect("order_success")

    return render(
        request,
        "orders/checkout.html",
        {
            "form": form,
            "cart": cart,
            "total": total,
            "packaging_charge": packaging_charge,
            "delivery_charge": delivery_charge,
            "grand_total": grand_total,
        },
    )
    
# ===========================
# My Orders
# ===========================

@customer_required
def my_orders(request):

    orders = Order.objects.filter(
        customer=request.user
    ).order_by("-created_at")

    return render(
        request,
        "orders/my_orders.html",
        {
            "orders": orders
        }
    )


# ===========================
# Track Order
# ===========================

@customer_required
def track_order(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        customer=request.user,
    )

    return render(
        request,
        "orders/track_order.html",
        {
            "order": order
        }
    )


# ===========================
# Order Success
# ===========================

@customer_required
def order_success(request):

    return render(
        request,
        "orders/order_success.html"
    )
