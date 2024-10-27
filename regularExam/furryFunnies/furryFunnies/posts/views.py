from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.views.generic.edit import BaseFormView

from furryFunnies.common.helpers import get_profile
from furryFunnies.posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from furryFunnies.posts.models import Post


class CreatePostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dash')

    def form_valid(self, form):
        form.instance.author = get_profile()

        return super().form_valid(form)


class DetailsPostView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'posts/details-post.html'


class EditPostView(UpdateView):
    model = Post
    pk_url_kwarg = 'post_id'
    form_class = PostEditForm
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dash')


class DeletePostView(DeleteView, BaseFormView):
    model = Post
    pk_url_kwarg = 'post_id'
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dash')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
