from django.shortcuts import render

from petstagram.photos.models import Photo


def home_page(request):
    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, 'common/home-page.html', context)
