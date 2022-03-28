from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as room_models

# Register your models here.


class RoomInline(admin.TabularInline):

    model = room_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Customer User Admin"""

    inlines = (RoomInline,)

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

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
    list_filter = UserAdmin.list_filter + ("superhost",)
