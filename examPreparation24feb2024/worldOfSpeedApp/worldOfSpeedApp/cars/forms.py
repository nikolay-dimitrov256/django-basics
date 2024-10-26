from django import forms

from worldOfSpeedApp.cars.models import Car


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
