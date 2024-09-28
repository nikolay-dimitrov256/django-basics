from django.db import models
from django.utils.text import slugify

from petstagram.accounts.models import User


class Pet(models.Model):
    name = models.CharField(
        max_length=30,
    )

    pet_photo = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    slug = models.CharField(
        max_length=100,
        blank=True,
    )

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='pets',
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
