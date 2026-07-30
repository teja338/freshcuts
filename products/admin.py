from django.contrib import admin
from .models import Category, Product


# ===========================
# Category Admin
# ===========================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "created_at",
    )

    list_display_links = (
        "name",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "id",
    )


# ===========================
# Product Admin
# ===========================

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "category",
        "product_type",
        "price",
        "stock",
        "is_featured",
        "is_active",
    )

    list_display_links = (
        "name",
    )

    list_filter = (
        "category",
        "product_type",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    list_editable = (
        "price",
        "stock",
        "is_featured",
        "is_active",
    )

    ordering = (
        "id",
    )

    list_per_page = 10

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "category",
                    "product_type",
                    "description",
                )
            },
        ),

        (
            "Pricing",
            {
                "fields": (
                    "price",
                    "original_price",
                    "discount_percentage",
                )
            },
        ),

        (
            "Inventory",
            {
                "fields": (
                    "stock",
                    "weight",
                    "image",
                )
            },
        ),

        (
            "Ratings",
            {
                "fields": (
                    "rating",
                    "reviews",
                )
            },
        ),

        (
            "Status",
            {
                "fields": (
                    "is_featured",
                    "is_active",
                )
            },
        ),

        (
            "Dates",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
