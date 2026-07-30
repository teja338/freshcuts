from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import User


# ==========================
# Register
# ==========================
def register(request):

    if request.user.is_authenticated:
        return redirect("home")

    form = RegisterForm()

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # Every new user becomes Customer
            user.role = User.CUSTOMER

            user.save()

            messages.success(
                request,
                "Registration Successful. Please Login."
            )

            return redirect("login")

    context = {
        "form": form
    }

    return render(
        request,
        "accounts/register.html",
        context
    )


# ==========================
# Login
# ==========================
def login_view(request):

    if request.user.is_authenticated:

        return redirect_user(request.user)

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect_user(user)

        else:

            messages.error(
                request,
                "Invalid Username or Password."
            )

    return render(
        request,
        "accounts/login.html"
    )


# ==========================
# Logout
# ==========================
@login_required
def logout_view(request):

    logout(request)

    messages.success(
        request,
        "Logged Out Successfully."
    )

    return redirect("login")


## ==========================
# Redirect According to Role
# ==========================
def redirect_user(user):

    if user.role == User.ADMIN:
        return redirect("admin_dashboard")

    elif user.role == User.WORKER:
        return redirect("worker_dashboard")

    else:
        return redirect("home")
