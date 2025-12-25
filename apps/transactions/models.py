from django.conf import settings
from django.db import models
from apps.accounts.models import Account
from apps.categories.models import Category
from django.core.exceptions import ValidationError


class Transaction(models.Model):
    INCOME = "IN"
    EXPENSE = "EX"

    TYPE_CHOICES = [
        (INCOME, "Ingreso"),
        (EXPENSE, "Egreso"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transactions"
    )
    account = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name="transactions"
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="transactions"
    )
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.amount <= 0:
            raise ValidationError("El monto debe ser mayor a cero")

        if self.category.type != self.type:
            raise ValidationError("La categoría no coincide con el tipo de transacción")

    class Meta:
        verbose_name = "Transacción"
        verbose_name_plural = "Transacciones"
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.get_type_display()} - {self.amount}"
