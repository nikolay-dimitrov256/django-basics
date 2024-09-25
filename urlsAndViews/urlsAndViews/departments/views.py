from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from urlsAndViews.departments.models import Department


def index(request):
    return HttpResponse('<h1>Hello World!</h1>')


def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f'<h1>Args: {args}, Kwargs: {kwargs}</h1>')


def view_with_variable(request, param):  # variable name should be named the same as in urls
    return HttpResponse(f'<h1>Variable: {param}</h1>')


def view_with_integer(request, pk):
    return HttpResponse(f'<h1>Pk: {pk}</h1>')


def view_department(request, pk, slug):
    department = Department.objects.filter(id=pk, slug=slug).first()

    return HttpResponse(f'<h1>Department: {department}</h1>')


def view_with_slug(request, slug):
    # department = Department.objects.filter(slug=slug).first()
    #
    # if not department:
    #     raise Http404

    department = get_object_or_404(Department, slug=slug)

    return HttpResponse(f'<h1>Department: {department}</h1>')


def show_archive(request, archive_year):
    return HttpResponse(f'<h1>The year is: {archive_year}</h1>')


def redirect_to_softuni(request):
    return redirect('https://softuni.bg')


def redirect_to_view(request):
    # return redirect('http://localhost:8000')  # breaks abstraction
    # return redirect(index)  # not ideal

    return redirect('home')  # best way
