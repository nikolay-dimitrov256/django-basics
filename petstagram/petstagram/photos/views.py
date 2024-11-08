from django.shortcuts import render

from petstagram.photos.models import Photo


def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    likes = photo.likes.all()
    comments = photo.comments.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
    }

    return render(request, 'photos/photo-details-page.html', context)


def edit_photo(request, pk: int):
    return render(request, 'photos/photo-edit-page.html')
