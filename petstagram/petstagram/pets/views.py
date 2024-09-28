from django.shortcuts import render


def add_pet_view(request):
    return render(request, 'pets/pet-add-page.html')


def pet_details_view(request, username, pet_slug):
    return render(request, 'pets/pet-details-page.html')


def pet_edit_view(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')


def pet_delete_view(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')
