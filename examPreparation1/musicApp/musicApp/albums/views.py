from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from musicApp.albums.forms import AlbumCreateForm
from musicApp.albums.models import Album
from musicApp.common.utils import get_profile


class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        album = form.save(commit=False)
        profile = get_profile()
        album.owner = profile
        album.save()

        return super().form_valid(form)


class AlbumDetailsView(DetailView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'albums/album-details.html'
