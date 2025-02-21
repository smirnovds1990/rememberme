from django.db import models

from .constants import (
    MAX_ARTICLE_TITLE_LENGTH,
    MAX_TAG_NAME_LENGTH,
    MAX_TOPIC_NAME_LENGTH,
)


class Article(models.Model):
    """Provides the article structure."""

    title = models.CharField(
        max_length=MAX_ARTICLE_TITLE_LENGTH,
        unique=True,
        blank=False,
        null=False,
    )
    content = models.TextField(blank=False, null=False)
    topic = models.ForeignKey(
        "Topic",
        on_delete=models.PROTECT,
        related_name="articles",
        blank=False,
    )
    tags = models.ManyToManyField("Tag", related_name="articles", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Topic(models.Model):
    """Describes what is an article about. One Article can have only one topic."""

    name = models.CharField(
        max_length=MAX_TOPIC_NAME_LENGTH, unique=True, blank=False, null=False
    )


class Tag(models.Model):
    """Provides tags to tag an article for more clearness."""

    name = models.CharField(
        max_length=MAX_TAG_NAME_LENGTH, unique=True, blank=False, null=False
    )
