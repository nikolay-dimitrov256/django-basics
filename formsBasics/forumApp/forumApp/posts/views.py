from datetime import datetime
from django.shortcuts import render, redirect

from forumApp.posts.forms import PersonForm, PostForm
from forumApp.posts.models import Post


def index(request):
    form = PersonForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data['person_name'])

    context = {
        'my_form': form,
    }

    return render(request, 'base.html', context)


def dashboard(request):
    posts = Post.objects.all()
    form = PostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        'posts': posts,
        'form': form
    }

    return render(request, 'posts/dashboard.html', context)
