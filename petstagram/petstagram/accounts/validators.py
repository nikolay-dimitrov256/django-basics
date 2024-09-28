from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class IsAlphaValidator:
    def __init__(self, message=''):
        self.message = message

    def __call__(self, value: str):
        if not value.isalpha():
            raise ValidationError(self.message)
