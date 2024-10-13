from django.db import models

from petstagram.photos.models import Photo


class Comment(models.Model):
    text = models.TextField(
        max_length=300,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    to_photo = models.ForeignKey(
        to=Photo,
        related_name='comments',
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        to=Photo,
        related_name='likes',
        on_delete=models.CASCADE,
    )
