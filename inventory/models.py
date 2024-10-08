# inventory/models.py
from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
