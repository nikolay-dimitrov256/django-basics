from django.http import HttpResponse
from django.shortcuts import render

from djangoIntroduction.todo_app.models import Task


def index(request):
    title_filter = request.GET.get('title_filter', '')

    tasks = Task.objects.filter(name__icontains=title_filter)

    context = {
        'tasks': tasks,
        'title_filter': title_filter,
    }

    return render(request, 'todo/index.html', context)
