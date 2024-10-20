from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect

from forumApp.posts.forms import PersonForm, PostCreateForm, PostDeleteForm, PostEditForm, SearchForm
from forumApp.posts.models import Post


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

    return render(request, 'common/index.html')


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
    form = PostCreateForm(request.POST or None)

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
    post = Post.objects.get(pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'posts/post-details.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)

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
