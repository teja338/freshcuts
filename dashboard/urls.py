from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "about/",
        views.about,
        name="about",
    ),

    path(
        "contact/",
        views.contact,
        name="contact",
    ),

    path(
        "admin/",
        views.admin_dashboard,
        name="admin_dashboard",
    ),

    path(
        "customer/",
        views.customer_dashboard,
        name="customer_dashboard",
    ),

    path(
        "worker/",
        views.worker_dashboard,
        name="worker_dashboard",
    ),

]
