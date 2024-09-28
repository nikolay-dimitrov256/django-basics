from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxSizeValidator:
    def __init__(self, limit_in_mb: int, message=''):
        self.message = message
        self.limit_in_mb = limit_in_mb

    def __call__(self, value):
        if value.size > self.limit_in_mb * 1024 * 1024:
            raise ValidationError(self.message)
