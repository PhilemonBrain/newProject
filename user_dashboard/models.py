from django.db import models

# Create your models here.

class apiBox(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    stats = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title