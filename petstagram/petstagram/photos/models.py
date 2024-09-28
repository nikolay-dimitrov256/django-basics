from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.accounts.models import User
from petstagram.pets.models import Pet
from petstagram.photos.validators import MaxSizeValidator


class Photo(models.Model):
    picture = models.ImageField(
        validators=[
            MaxSizeValidator(5, message='Image size cannot be more than 5MB.'),
        ],
    )

    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(10)
        ],
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    tagged_pets = models.ManyToManyField(
        to=Pet,
    )

    published_on = models.DateField(
        auto_now_add=True,
        blank=True,
    )

    likes = models.ManyToManyField(
        to=User,
        through='Like',
    )


class Comment(models.Model):
    text = models.TextField(
        max_length=300,
    )

    published_on = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )

    photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    photo_id = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
    )

    user_id = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = [
            ['photo_id', 'user_id']
        ]
