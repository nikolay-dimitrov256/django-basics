from django.core.validators import MinLengthValidator
from django.db import models

from forumApp.posts.choices import LanguageChoices


class Post(models.Model):
    TITLE_MAX_LENGTH = 100
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    content = models.TextField(
        validators=[MinLengthValidator(5)]
    )

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
