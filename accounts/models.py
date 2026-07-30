from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ADMIN = "ADMIN"
    WORKER = "WORKER"
    CUSTOMER = "CUSTOMER"

    ROLE_CHOICES = (
        (ADMIN, "Admin"),
        (WORKER, "Worker"),
        (CUSTOMER, "Customer"),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=CUSTOMER
    )

    phone = models.CharField(
        max_length=15,
        unique=True
    )

    address = models.TextField(blank=True)

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
