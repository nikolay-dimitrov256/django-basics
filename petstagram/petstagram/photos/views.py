from django.shortcuts import render


def add_photo_view(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details_view(request, pk):
    return render(request, 'photos/photo-details-page.html')


def edit_photo_view(request, pk):
    return render(request, 'photos/photo-edit-page.html')
