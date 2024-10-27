from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from furryFunnies.posts.models import Post


class IndexView(TemplateView):
    template_name = 'common/index.html'


class DashboardView(ListView):
    model = Post
    template_name = 'common/dashboard.html'
