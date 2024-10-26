from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from worldOfSpeedApp.common.helpers import get_profile
from worldOfSpeedApp.profiles.forms import ProfileCreateForm
from worldOfSpeedApp.profiles.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/profile-create.html'
    success_url = reverse_lazy('catalogue')


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return Profile.objects.annotate(total_sum=Sum('cars__price')).first()
