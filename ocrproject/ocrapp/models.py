from django.db import models

# Create your models here.
class OcrModel(models.Model):
    image = models.FileField(upload_to="images/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

