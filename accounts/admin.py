from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "FreshCuts",
            {
                "fields": (
                    "role",
                    "phone",
                    "address",
                    "profile_image",
                )
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "phone",
        "role",
        "is_staff",
    )

    list_filter = (
        "role",
        "is_staff",
    )
