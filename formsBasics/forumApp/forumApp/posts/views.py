from datetime import datetime

from django.db.models import Q
from django.forms import modelform_factory
from django.http import Http404
from django.shortcuts import render, redirect
from django import views
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, FormView, ListView

from forumApp.posts.forms import PersonForm, PostCreateForm, PostDeleteForm, PostEditForm, SearchForm, CommentFormSet
from forumApp.posts.models import Post, Comment


class IndexView(TemplateView):
    template_name = 'common/index.html'


class DashboardView(ListView, FormView):
    model = Post
    context_object_name = 'posts'
    form_class = SearchForm
    paginate_by = 2
    template_name = 'posts/dashboard.html'

    def get_queryset(self):
        queryset = self.model.objects.all()

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            search = Q(title__icontains=query) | Q(content__icontains=query)
            queryset = queryset.filter(search)

        return queryset


class AddPostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    # success_url = reverse_lazy('dash')

    def get_success_url(self):
        return reverse_lazy('post_details', kwargs={'pk': self.object.pk})


class EditPostView(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'posts/edit-post.html'
    # success_url = reverse_lazy('dash')

    def get_success_url(self):
        return reverse_lazy('post_details', kwargs={'pk': self.object.pk})


class DeletePostView(DeleteView, FormView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dash')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Post.objects.get(pk=pk)
        return post.__dict__


class PostDetailsView(DetailView):
    model = Post
    template_name = 'posts/post-details.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)

        try:
            obj = Post.objects.prefetch_related('comments').get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = CommentFormSet()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        formset = CommentFormSet(request.POST or None)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('post_details', pk=post.pk)

        context = self.get_context_data()
        context['formset'] = formset

        return self.render_to_response(context)


def index(request):
    # form = PersonForm(request.POST or None)
    #
    # if request.method == 'POST':
    #     if form.is_valid():
    #         print(form.cleaned_data['person_name'])
    #
    # context = {
    #     'my_form': form,
    # }

    post_form = modelform_factory(Post, fields=['title', 'content'])

    context = {
        'form': post_form,
    }

    return render(request, 'common/index.html', context)


def dashboard(request):
    form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == 'GET':
        if form.is_valid():
            query = form.cleaned_data['query']
            search = Q(title__icontains=query) | Q(content__icontains=query)
            posts = posts.filter(search)

    context = {
        'posts': posts,
        'form': form,
    }

    return render(request, 'posts/dashboard.html', context)


def add_post(request):
    form = PostCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        'form': form
    }

    return render(request, 'posts/add-post.html', context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == 'POST':
        post.delete()
        return redirect('dash')

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'posts/delete-post.html', context)


def post_details(request, pk: int):
    post = Post.objects.prefetch_related('comments').get(pk=pk)
    comments = post.comments.all()
    formset = CommentFormSet(request.POST or None)

    if request.method == 'POST':
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('post_details', pk=pk)

    context = {
        'post': post,
        'formset': formset,
        'comments': comments
    }

    return render(request, 'posts/post-details.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostEditForm(request.POST, request.FILES or None, instance=post)

        if form.is_valid():
            form.save()
            return redirect('post_details', pk=pk)
    else:
        form = PostEditForm(instance=post)

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'posts/edit-post.html', context)
