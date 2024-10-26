from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django.views.generic.edit import BaseFormView

from musicApp.albums.models import Album
from musicApp.common.utils import get_profile
from musicApp.profiles.forms import ProfileCreateForm
from musicApp.profiles.models import Profile


class HomeView(ListView, BaseFormView):
    model = Album
    context_object_name = 'albums'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        profile = get_profile()

        if profile is None:
            return ['common/home-no-profile.html']

        return ['common/home-with-profile.html']

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['profile'] = get_profile()

        return context

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)
