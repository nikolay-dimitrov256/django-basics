from django import forms

from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'personal_photo', 'date_of_birth']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'personal_photo': forms.URLInput(attrs={'placeholder': 'Pet Image URL'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(PetBaseForm):
    pass
