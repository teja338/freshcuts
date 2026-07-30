from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def customer_required(view_func):
    @login_required
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.role != "CUSTOMER":
            messages.error(request, "Access Denied!")
            return redirect("home")

        return view_func(request, *args, **kwargs)

    return wrapper


def admin_required(view_func):
    @login_required
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.role != "ADMIN":
            messages.error(request, "Access Denied!")
            return redirect("home")

        return view_func(request, *args, **kwargs)

    return wrapper


def worker_required(view_func):
    @login_required
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.role != "WORKER":
            messages.error(request, "Access Denied!")
            return redirect("home")

        return view_func(request, *args, **kwargs)

    return wrapper
