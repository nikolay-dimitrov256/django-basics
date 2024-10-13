from django import forms


class PersonForm(forms.Form):
    STATUS_CHOICES = (
        (1, 'Published'),
        (2, 'Draft'),
        (3, 'Archived')
    )

    person_name = forms.CharField(
        max_length=10,
        label='Fill in person name:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your name here...'
            }
        )
    )

    age = forms.IntegerField()

    # status = forms.IntegerField(
    #     widget=forms.Select(
    #         choices=STATUS_CHOICES
    #     )
    # )

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.RadioSelect(),
    )
