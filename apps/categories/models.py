from django.conf import settings
from django.db import models


class Category(models.Model):
    INCOME = "IN"
    EXPENSE = "EX"

    TYPE_CHOICES = [
        (INCOME, "Ingreso"),
        (EXPENSE, "Egreso"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="categories"
    )
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        unique_together = ("user", "name", "type")
        ordering = ["type", "name"]

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
