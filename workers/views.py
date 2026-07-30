from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from orders.models import Order


@login_required
def worker_dashboard(request):

    orders = Order.objects.filter(worker=request.user).order_by("-created_at")

    context = {
        "orders": orders,
        "assigned_orders": orders.count(),
        "delivered_orders": orders.filter(status="Delivered").count(),
        "pending_orders": orders.exclude(status="Delivered").count(),
    }

    return render(
        request,
        "workers/dashboard.html",
        context,
    )


@login_required
def worker_order_detail(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        worker=request.user,
    )

    return render(
        request,
        "workers/order_detail.html",
        {"order": order},
    )
@login_required
def update_order_status(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        worker=request.user,
    )

    if request.method == "POST":
        status = request.POST.get("status")

        valid_status = [
            "Accepted",
            "Preparing",
            "Out for Delivery",
            "Delivered",
        ]

        if status in valid_status:
            order.status = status
            order.save()

    return redirect("worker_order_detail", order_id=order.id)
