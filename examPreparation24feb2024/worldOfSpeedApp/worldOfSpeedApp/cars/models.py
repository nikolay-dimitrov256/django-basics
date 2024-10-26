from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from worldOfSpeedApp.cars.choices import CarTypeChoices


class Car(models.Model):
    type = models.CharField(
        max_length=10,
        choices=CarTypeChoices.choices,
    )

    model = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(1),
        ],
    )

    year = models.IntegerField(
        validators=[
            MinValueValidator(1999, message='Year must be between 1999 and 2030!'),
            MaxValueValidator(2030, message='Year must be between 1999 and 2030!'),
        ],
    )

    image_url = models.URLField(
        unique=True,
        error_messages={'unique': 'This image URL is already in use! Provide a new one.'},
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(1.0)
        ]
    )

    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='cars',
    )
