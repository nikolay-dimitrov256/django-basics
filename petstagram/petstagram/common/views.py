from django.shortcuts import render, redirect

from petstagram.common.models import Like
from petstagram.photos.models import Photo


def home_page(request):
    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    like_object = Like.objects.filter(to_photo_id=photo_id).first()

    if like_object:
        like_object.delete()
    else:
        like = Like(to_photo_id=photo_id)
        like.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')
