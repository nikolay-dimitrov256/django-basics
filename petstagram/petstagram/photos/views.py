from django.shortcuts import render

from petstagram.photos.models import Photo


def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk: int):
    return render(request, 'photos/photo-details-page.html')


def edit_photo(request, pk: int):
    return render(request, 'photos/photo-edit-page.html')
