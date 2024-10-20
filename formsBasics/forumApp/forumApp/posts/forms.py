from django import forms
from django.core.exceptions import ValidationError

from forumApp.posts.mixins import DisableFieldsMixin
from forumApp.posts.models import Post, Comment


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
        error_messages = {
            'title': {
                'required': 'Please enter a title',
                'max_length': f'The title shouldn\'t be longer than {Post.TITLE_MAX_LENGTH} characters'
            },
            'author': {
                'required': 'Please enter an author'
            }
        }

    def clean_author(self):
        author = self.cleaned_data.get('author')

        if author and not author[0].isupper():
            raise ValidationError('Author name should start with capital letter!')

        return author

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if not title[0].isupper():
            raise ValidationError('Title should start with a capital letter!')

        return title

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content and 'hello' in title.lower() and 'hello' in content.lower():
            raise ValidationError('You can only greet once!')

        return cleaned_data

    def save(self, commit=True):
        post = super().save()

        post.content = post.content.capitalize()

        if commit:
            post.save()

        return post  # returning is optional


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(DisableFieldsMixin, PostBaseForm):
    # disabled_fields = ('title', 'author')
    pass


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        # error_messages={
        #     'required': 'Please enter search words',
        # },
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search'
            }
        )
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content',)

        labels = {
            'author': '',
            'content': '',
        }

        error_messages = {
            'author': {
                'required': 'Who are you?'
            },
            'content': {
                'required': 'Please say something'
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name here',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Say something'
        })


CommentFormSet = forms.formset_factory(CommentForm, extra=3)
