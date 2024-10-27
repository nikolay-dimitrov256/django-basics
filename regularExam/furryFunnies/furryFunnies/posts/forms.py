from django import forms

from furryFunnies.posts.mixins import ReadonlyMixin
from furryFunnies.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['updated_at', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder:': 'Put an attractive and unique title...', 'label': 'Title:'}),
            'image_url': forms.URLInput(attrs={'label': 'Post Image URL:'}),
            'content': forms.Textarea(
                attrs={'placeholder:': 'Share some interesting facts about your adorable pets...', 'label': 'Content:'}),
        }


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(ReadonlyMixin, PostBaseForm):
    pass
