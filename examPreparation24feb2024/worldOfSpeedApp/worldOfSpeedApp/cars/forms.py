from django import forms

from worldOfSpeedApp.cars.models import Car
from worldOfSpeedApp.common.mixins import ReadonlyMixin


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'})
        }


class CarCreateForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(ReadonlyMixin, CarBaseForm):
    pass
