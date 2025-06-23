from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

class Part(models.Model):
    part_number = models.CharField(max_length=100, unique=True)  # Unique ID for the part
    name = models.CharField(max_length=255)                      # Human-readable name
    version = models.CharField(max_length=10)                    # Version like v1, v2
    description = models.TextField(blank=True)                   # Optional notes
    created_at = models.DateTimeField(auto_now_add=True)         # Timestamp
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    # Links to the user who created the part

    def __str__(self):
        return f"{self.part_number} - v{self.version}"
