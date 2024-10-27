from django import forms

from furryFunnies.authors.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),
        }
        labels = {
            'passcode': 'Passcode:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'pets_number': 'Pets Number:',
            'info': 'Info:',
            'image_url': 'Profile Image URL:',
        }


class AuthorCreateForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        exclude = ['info', 'image_url']


class AuthorEditForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        exclude = ['passcode']
