from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from worldOfSpeedApp.cars.forms import CarCreateForm
from worldOfSpeedApp.cars.models import Car
from worldOfSpeedApp.common.helpers import get_profile


class CreateCarView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('index')  # TODO: Change to 'catalogue'

    def form_valid(self, form):
        form.instance.owner = get_profile()

        return super().form_valid(form)
