from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from accounts.decorators import admin_required
from .models import Product, Category
from .forms import ProductForm


# --------------------------
# Product List
# --------------------------
def product_list(request):

    products = Product.objects.filter(
        is_active=True
    ).select_related("category")

    search = request.GET.get("search", "")
    category = request.GET.get("category", "")
    product_type = request.GET.get("type", "")
    sort = request.GET.get("sort", "")

    # Search
    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )

    # Filter from Home Page Categories
    if category:
        products = products.filter(
            product_type=category
        )

    # Filter from Product Type Dropdown
    if product_type:
        products = products.filter(
            product_type=product_type
        )

    # Sorting
    if sort == "price_low":
        products = products.order_by("price")

    elif sort == "price_high":
        products = products.order_by("-price")

    elif sort == "newest":
        products = products.order_by("-created_at")

    elif sort == "name":
        products = products.order_by("name")

    # Pagination
    paginator = Paginator(products, 8)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "products": page_obj,
        "categories": Category.objects.all(),
        "featured_products": Product.objects.filter(
            is_active=True,
            is_featured=True
        )[:4],
        "search": search,
        "selected_category": category,
        "selected_type": product_type,
        "selected_sort": sort,
    }

    return render(
        request,
        "products/products.html",
        context
    )

# --------------------------
# Product Detail
# --------------------------

def product_detail(request, id):

    product = get_object_or_404(
        Product,
        id=id,
        is_active=True
    )

    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(
        id=product.id
    )[:4]

    context = {
        "product": product,
        "related_products": related_products,
    }

    return render(
        request,
        "products/product_detail.html",
        context
    )


# --------------------------
# Add Product
# --------------------------

@admin_required
def add_product(request):

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Product added successfully."
            )

            return redirect("products")

    else:

        form = ProductForm()

    return render(
        request,
        "products/add_product.html",
        {
            "form": form
        }
    )


# --------------------------
# Edit Product
# --------------------------

@admin_required
def edit_product(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Product updated successfully."
            )

            return redirect("products")

    else:

        form = ProductForm(
            instance=product
        )

    return render(
        request,
        "products/edit_product.html",
        {
            "form": form,
            "product": product,
        }
    )


# --------------------------
# Delete Product
# --------------------------

@admin_required
def delete_product(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    if request.method == "POST":

        product.delete()

        messages.success(
            request,
            "Product deleted successfully."
        )

        return redirect("products")

    return render(
        request,
        "products/delete_product.html",
        {
            "product": product
        }
    )
