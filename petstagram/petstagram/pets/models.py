from django.db import models
# from django.template.defaultfilters import slugify
from django.utils.text import slugify


class Pet(models.Model):
    name = models.CharField(
        max_length=30,
    )

    personal_photo = models.URLField()

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True,
        editable=False,
        allow_unicode=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}', allow_unicode=True)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
