from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "user", "is_active")
    list_filter = (
        "type",
        "is_active",
    )
