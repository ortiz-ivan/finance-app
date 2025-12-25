from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "balance", "is_active")
    list_filter = ("is_active",)
