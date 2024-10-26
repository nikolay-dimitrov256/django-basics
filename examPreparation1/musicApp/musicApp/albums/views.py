from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from musicApp.albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from musicApp.albums.models import Album
from musicApp.common.utils import get_profile


class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_profile()

        return super().form_valid(form)


class AlbumDetailsView(DetailView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'albums/album-details.html'


class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumEditForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    template_name = 'albums/album-edit.html'


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    template_name = 'albums/album-delete.html'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
