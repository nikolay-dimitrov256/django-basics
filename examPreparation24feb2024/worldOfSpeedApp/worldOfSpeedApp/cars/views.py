from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from worldOfSpeedApp.cars.forms import CarCreateForm
from worldOfSpeedApp.cars.models import Car
from worldOfSpeedApp.common.helpers import get_profile


class CreateCarView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.owner = get_profile()

        return super().form_valid(form)


class CatalogueView(ListView):
    model = Car
    template_name = 'cars/catalogue.html'

    def get_queryset(self):
        profile = get_profile()

        return Car.objects.filter(owner=profile)
