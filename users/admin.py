from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Customer User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Proflie",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = (
        "language",
        "currency",
        "superhost",
    )
