from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddKitForm, AddDrugForm
from .models import Kit, Drug


def index(request):
    context = {
        'kits': Kit.objects.all(),
    }

    return render(request, 'medikit/home.html', context)


def edit(request, item_type):
    item_types = {
        'kit': {
            'form': AddKitForm,
            'items': Kit.objects.all()
        },
        'drug': {
            'form': AddDrugForm,
            'items': Drug.objects.all()
        },
    }

    if request.method == 'POST':
        form = item_types[item_type]['form'](data=request.POST)
        if form.is_valid():
            form.save()

    context = {
        'item_type': item_type,
        'form': item_types[item_type]['form'],
        'items': item_types[item_type]['items'],
    }

    return render(request, 'medikit/edit_all_items.html', context)


def edit_one(request, item_type, item_id):
    item_types = {
        'kit': {
            'form': AddKitForm,
            'class': Kit,
        },
        'drug': {
            'form': AddDrugForm,
            'class': Drug,
        },
    }

    item = get_object_or_404(item_types[item_type]['class'], id=item_id)

    saved = False
    if request.method == 'POST':
        form = item_types[item_type]['form'](data=request.POST, instance=item)
        if form.is_valid():
            form.save()
            saved = True
    else:
        form = item_types[item_type]['form'](instance=item)

    context = {
        'item_type': item_type,
        'form': form,
        'saved': saved,
    }

    return render(request, 'medikit/edit_one_item.html', context)


def remove(request, item_type, item_id):
    item_types = {
        'kit': {
            'form': AddKitForm,
            'class': Kit,
        },
        'drug': {
            'form': AddDrugForm,
            'class': Drug,
        },
    }

    item = get_object_or_404(item_types[item_type]['class'], id=item_id)
    item.delete()

    return redirect('medikit:edit', item_type=item_type)
