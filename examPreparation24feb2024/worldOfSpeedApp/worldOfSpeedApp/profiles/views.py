from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from worldOfSpeedApp.common.helpers import get_profile
from worldOfSpeedApp.profiles.forms import ProfileCreateForm, ProfileEditForm
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


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profiles/profile-edit.html'
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        return get_profile()


class ProfileDeleteView(DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()
