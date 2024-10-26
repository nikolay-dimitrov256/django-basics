from django.shortcuts import render
from django.views.generic import TemplateView

from worldOfSpeedApp.common.helpers import get_profile


class IndexView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()

        return context
