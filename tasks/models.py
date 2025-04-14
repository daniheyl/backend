from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.name} (Order: {self.order})"

    def clean(self):
        """Validate that order is positive"""
        if self.order < 0:
            raise ValidationError("Order must be a positive number")

    def save(self, *args, **kwargs):
        """Override save to ensure clean() is called"""
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Statuses"
        ordering = ['order']
        db_table = 'tasks_status'  # Explicit table name to prevent any naming issues


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='tasks',
        verbose_name='Task Status'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        null=False,
        blank=False,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.status.name if self.status else 'No Status'}"

    def save(self, *args, **kwargs):
        """Override save to ensure validation"""
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Tasks"
        indexes = [
            models.Index(fields=['user', 'status']),
            models.Index(fields=['created_at']),
        ]
