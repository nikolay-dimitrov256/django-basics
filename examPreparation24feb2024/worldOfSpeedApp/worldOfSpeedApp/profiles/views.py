from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from worldOfSpeedApp.profiles.forms import ProfileCreateForm
from worldOfSpeedApp.profiles.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/profile-create.html'
    success_url = reverse_lazy('index')  # TODO: Change to 'catalogue'
