from django.shortcuts import render

from .forms import AddKitForm, AddDrugForm
from .models import Kit


def index(request):
    context = {
        'kits': Kit.objects.all(),
    }

    return render(request, 'medikit/index.html', context=context)


def items_add(request, item):
    form_vars = {
        'kit': {
            'form': AddKitForm,
        },
        'drug': {
            'form': AddDrugForm,
        }
    }

    if request.method == 'POST':
        form = form_vars[item]['form'](data=request.POST)
        if form.is_valid():
            form.save()
            form = form_vars[item]['form']()
    else:
        form = form_vars[item]['form']()

    context = {
        'form': form,
        'item': item,
    }

    return render(request, 'medikit/items_add.html', context)

