from django import forms

from musicApp.albums.models import Album
from musicApp.common.mixins import ReadonlyMixin


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(ReadonlyMixin, AlbumBaseForm):
    pass
