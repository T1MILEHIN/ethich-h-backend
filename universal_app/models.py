import uuid
from django.db import models
from django.conf import settings

# Create your models here.

class UniversalFormInput(models.Model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=255)
    field_value = models.TextField()
    unique_link = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    def __str__(self):
        return f"{self.users.username} - {self.field_name}"
    
    def get_absolute_url(self):
        return f"/access-data/{self.unique_link}/"
