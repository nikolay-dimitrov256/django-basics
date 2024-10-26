from django.db.models import TextChoices


class CarTypeChoices(TextChoices):
    RALLY = 'Rally', 'Rally'
    OPEN_WHEEL = 'Open-wheel', 'Open-wheel'
    KART = 'Kart', 'Kart'
    DRAG = 'Drag', 'Drag'
    OTHER = 'Other', 'Other'
