from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from orders.models import Order
from products.models import Product


# -----------------------------
# Home Page
# -----------------------------
def home(request):
    products = Product.objects.filter(is_active=True)[:8]

    context = {
        "products": products
    }

    return render(request, "home.html", context)


# -----------------------------
# Customer Dashboard
# -----------------------------
@login_required
def customer_dashboard(request):

    if request.user.role != "CUSTOMER":
        return HttpResponseForbidden("Access Denied")

    orders = Order.objects.filter(
        customer=request.user
    ).order_by("-created_at")

    context = {
        "orders": orders
    }

    return render(
        request,
        "dashboard/customer_dashboard.html",
        context,
    )
# -----------------------------
# Admin Dashboard
# -----------------------------
@login_required
def admin_dashboard(request):

    if request.user.role != "ADMIN":
        return HttpResponseForbidden("Access Denied")

    total_products = Product.objects.count()
    total_orders = Order.objects.count()

    pending_orders = Order.objects.filter(
        status="Pending"
    ).count()

    delivered_orders = Order.objects.filter(
        status="Delivered"
    ).count()

    total_customers = Order.objects.values(
        "customer"
    ).distinct().count()

    total_revenue = (
        sum(order.total for order in Order.objects.all())
        if total_orders > 0 else 0
    )

    recent_orders = Order.objects.select_related(
        "customer"
    ).order_by("-created_at")[:10]

    context = {
        "total_products": total_products,
        "total_orders": total_orders,
        "pending_orders": pending_orders,
        "delivered_orders": delivered_orders,
        "total_customers": total_customers,
        "total_revenue": total_revenue,
        "recent_orders": recent_orders,
    }

    return render(
        request,
        "dashboard/admin_dashboard.html",
        context,
    )

# -----------------------------
# Worker Dashboard
# -----------------------------
@login_required
def worker_dashboard(request):

    if request.user.role != "WORKER":
        return HttpResponseForbidden("Access Denied")

    assigned_orders = Order.objects.filter(
        worker=request.user
    ).order_by("-created_at")

    context = {
        "assigned_orders": assigned_orders
    }

    return render(
        request,
        "dashboard/worker_dashboard.html",
        context,
    )
    
    # -----------------------------
# About Page
# -----------------------------
def about(request):
    return render(request, "dashboard/about.html")


# -----------------------------
# Contact Page
# -----------------------------
def contact(request):
    return render(request, "dashboard/contact.html")
