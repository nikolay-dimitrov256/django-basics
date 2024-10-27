from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def letters_validator(value: str):
    if not value.isalpha():
        raise ValidationError('Your name must contain letters only!')


@deconstructible
class ExactLengthPasswordValidator:
    def __init__(self, required_length, message=None):
        self.required_length = required_length
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f'Your passcode must be exactly {self.required_length} digits!'
        else:
            self.__message = value

    def __call__(self, value: str):
        if len(value) != self.required_length:
            raise ValidationError(self.message)

        if not value.isdigit():
            raise ValidationError(self.message)
