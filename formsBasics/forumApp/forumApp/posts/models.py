from django.db import models

from forumApp.posts.choices import LanguageChoices


class Post(models.Model):
    title = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    author = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )

    language = models.CharField(
        max_length=20,
        choices=LanguageChoices.choices,
        default=LanguageChoices.OTHER,
    )
