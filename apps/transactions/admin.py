from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("type", "amount", "category", "account", "date", "user")
    list_filter = (
        "type",
        "date",
    )
