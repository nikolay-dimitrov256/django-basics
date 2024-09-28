from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.accounts.validators import IsAlphaValidator
from petstagram.accounts.choices import GenderChoices


class User(models.Model):
    username = models.CharField(
        max_length=50,
    )

    password = models.CharField(
        max_length=100,
    )

    email_address = models.EmailField()

    first_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2, message='First name should be at least 2 letters long.'),
            IsAlphaValidator(message='First name should consist of only letters.'),
        ]
    )

    last_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2, message='Last name should be at least 2 letters long.'),
            IsAlphaValidator(message='Last name should consist of only letters.'),
        ]
    )

    profile_picture = models.URLField()

    gender = models.CharField(
        choices=GenderChoices.choices
    )