
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("staff", "Staff"),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="staff"
    )

    def __str__(self):
        return self.username

class Task(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="medium"
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="task_images/",
        blank=True,
        null=True
    )

    attachment = models.FileField(
        upload_to="task_files/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
