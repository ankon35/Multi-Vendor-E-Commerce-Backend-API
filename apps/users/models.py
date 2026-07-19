from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    Role_CHOICES = [
        ("customer", "Customer"),
        ("admin", "Admin"),
        ("vendor", "Vendor"),
    ]

    role = models.CharField(max_length=20, choices=Role_CHOICES, default="customer")

    def __str__(self):
        return f"{self.username} ({self.role})"