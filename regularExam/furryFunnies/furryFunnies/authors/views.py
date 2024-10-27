from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from furryFunnies.authors.forms import AuthorCreateForm, AuthorEditForm
from furryFunnies.authors.models import Author
from furryFunnies.common.helpers import get_profile


class CreateAuthorView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'authors/create-author.html'
    success_url = reverse_lazy('dash')


class DetailsAuthorView(DetailView):
    template_name = 'authors/details-author.html'

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = get_profile()
        posts = author.post_set.order_by('updated_at')
        context['author'] = author
        context['posts'] = posts

        return context


class EditAuthorView(UpdateView):
    form_class = AuthorEditForm
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('details-author')

    def get_object(self, queryset=None):
        return get_profile()


class DeleteAuthorView(DeleteView):
    template_name = 'authors/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()
