from django.shortcuts import render
from django.views.generic import DetailView

from musicApp.common.utils import get_profile
from musicApp.profiles.models import Profile


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_profile()