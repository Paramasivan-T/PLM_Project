from django.db import models
from parts.models import Part  # We assume your parts app has the Part model

class BOMItem(models.Model):
    parent = models.ForeignKey(
        Part,
        related_name='bom_parent',
        on_delete=models.CASCADE,
        help_text="The main part (assembly)"
    )
    child = models.ForeignKey(
        Part,
        related_name='bom_child',
        on_delete=models.CASCADE,
        help_text="Component that is part of the assembly"
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('parent', 'child')  # Prevent duplicate entries

    def __str__(self):
        return f"{self.parent} contains {self.quantity} x {self.child}"
