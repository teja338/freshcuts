from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.worker_dashboard,
        name="worker_dashboard",
    ),

    path(
        "order/<int:order_id>/",
        views.worker_order_detail,
        name="worker_order_detail",
    ),

    path(
        "order/<int:order_id>/update/",
        views.update_order_status,
        name="update_order_status",
    ),

]
