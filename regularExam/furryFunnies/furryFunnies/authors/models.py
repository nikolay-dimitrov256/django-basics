from django.core.validators import MinLengthValidator
from django.db import models

from furryFunnies.authors.validators import letters_validator, ExactLengthPasswordValidator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            letters_validator,
        ]
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            letters_validator,
        ]
    )

    passcode = models.CharField(
        max_length=6,
        validators=[
            ExactLengthPasswordValidator(6),
        ],
        help_text='Your passcode must be a combination of 6 digits',
    )

    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )
