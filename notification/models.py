from django.db import models

# Create your models here.

class Notification(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return self.details
