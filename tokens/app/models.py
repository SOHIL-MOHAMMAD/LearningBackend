from django.db import models
from django.conf import settings
import uuid
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.

class User(AbstractUser):
    pass


class RefreshToken(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="refresh_tokens"
    )

    token = models.TextField(unique=True)

    is_revoked = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    expires_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username}"