from django.db import models


class LanguageChoices(models.TextChoices):
    PYTHON = 'py', 'Python'
    JAVASCRIPT = 'js', 'JavaScript'
    C_PLUS_PLUS = 'cpp', 'C++'
    JAVA = 'jv', 'Java'
    OTHER = 'other', 'Other'
