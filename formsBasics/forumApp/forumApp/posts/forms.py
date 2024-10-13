from django import forms

from forumApp.posts.models import Post


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


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['created_at']
