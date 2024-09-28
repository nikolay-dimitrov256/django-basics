from django.db import models


class GenderChoices(models.TextChoices):
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
