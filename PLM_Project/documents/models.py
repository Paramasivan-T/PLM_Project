from django.db import models
from parts.models import Part

class Document(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)   # Link document to part
    file = models.FileField(upload_to='documents/')            # Uploaded file
    uploaded_at = models.DateTimeField(auto_now_add=True)      # Upload timestamp

    def __str__(self):
        return f"Document for {self.part} uploaded at {self.uploaded_at}"