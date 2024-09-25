from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'current_time': datetime.now(),
        'person': {
            'name': 'Nikolay',
            'age': 38,
        },
        'ids': ['34563256', 'dsf3546633', '33465564567'],
        'text': 'hello, my name is Nikolay and I am a developer.'
    }

    return render(request, 'base.html', context)
