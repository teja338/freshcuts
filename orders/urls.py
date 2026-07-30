from django.urls import path
from . import views

urlpatterns = [

    # ===========================
    # Cart
    # ===========================

    path(
        "cart/",
        views.cart,
        name="cart",
    ),

    path(
        "cart/add/<int:product_id>/",
        views.add_to_cart,
        name="add_to_cart",
    ),

    path(
        "cart/increase/<int:product_id>/",
        views.increase_quantity,
        name="increase_quantity",
    ),

    path(
        "cart/decrease/<int:product_id>/",
        views.decrease_quantity,
        name="decrease_quantity",
    ),

    path(
        "cart/remove/<int:product_id>/",
        views.remove_from_cart,
        name="remove_from_cart",
    ),

    # ===========================
    # Checkout
    # ===========================

    path(
        "checkout/",
        views.checkout,
        name="checkout",
    ),

    # ===========================
    # Orders
    # ===========================

    path(
        "my-orders/",
        views.my_orders,
        name="my_orders",
    ),

    path(
        "track/<int:order_id>/",
        views.track_order,
        name="track_order",
    ),
    path(
    "success/",
    views.order_success,
    name="order_success"
   ),

]
