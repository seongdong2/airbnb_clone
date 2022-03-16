from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """Customer User Admin"""

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = (
        "language",
        "currency",
        "superhost",
    )
