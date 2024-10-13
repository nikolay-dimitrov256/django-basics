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


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['created_at']
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'What\'s on your mind?'
                }
            )
        }


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True
