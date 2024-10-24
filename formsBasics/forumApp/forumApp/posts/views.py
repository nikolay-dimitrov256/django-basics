from datetime import datetime

from django.db.models import Q
from django.forms import modelform_factory
from django.shortcuts import render, redirect

from forumApp.posts.forms import PersonForm, PostCreateForm, PostDeleteForm, PostEditForm, SearchForm, CommentFormSet
from forumApp.posts.models import Post, Comment


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
