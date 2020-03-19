from django.shortcuts import render

from medikit.models import Kit


def index(request):
    context = {
        'kits': Kit.objects.all(),
    }

    return render(request, 'medikit/index.html', context=context)
