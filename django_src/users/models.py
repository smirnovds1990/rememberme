from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import MAX_PHONE_LENGTH


class User(AbstractUser):
    """Custom User model to have some extra fields."""

    topics = models.ManyToManyField(
        "articles.Topic", related_name="users", blank=True
    )
    messages_schedule = models.JSONField(blank=False, null=False, default=list)
    phone_number = models.CharField(
        blank=True, default="", max_length=MAX_PHONE_LENGTH
    )
