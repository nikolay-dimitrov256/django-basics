from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


class AddPetView(CreateView):
    model = Pet
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': 1})


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = self.object.photo_set.all()
        context['comment_form'] = CommentForm()

        return context


class EditPetView(UpdateView):
    model = Pet
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'
    template_name = 'pets/pet-edit-page.html'
    form_class = PetEditForm

    def get_success_url(self):
        return reverse_lazy('pet_details', kwargs={
            'username': self.kwargs['username'],
            'pet_slug': self.kwargs['pet_slug']
        })


class DeletePetView(DeleteView):
    model = Pet
    slug_url_kwarg = 'pet_slug'
    template_name = 'pets/pet-delete-page.html'
    form_class = PetDeleteForm
    success_url = reverse_lazy('profile_details', kwargs={'pk': 1})

    def get_initial(self):
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial()
        })

        return kwargs


def add_pet(request):
    form = PetCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile_details', pk=1)

    context = {
        'form': form,
    }

    return render(request, 'pets/pet-add-page.html', context)


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    photos = pet.photo_set.all()
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'photos': photos,
        'comment_form': comment_form,
    }

    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('pet_details', username, pet_slug)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetDeleteForm(instance=pet)

    if request.method == 'POST':
        pet.delete()

        return redirect('profile_details', pk=1)

    context = {
        'pet': pet,
        'form': form,
    }

    return render(request, 'pets/pet-delete-page.html', context)
