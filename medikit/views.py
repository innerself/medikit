from django import http
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import AddKitForm, AddMedicationForm
from .models import Kit, Medication


def home(request):
    if request.user.is_authenticated:
        context = {
            'kits': Kit.objects.filter(user__id=request.user.id),
        }
        return render(request, 'medikit/dashboard.html', context)
    else:
        return render(request, 'medikit/welcome.html', {})


@login_required
def edit_kits(request):
    if request.method == 'POST':
        form = AddKitForm(data=request.POST)
        if form.is_valid():
            new_kit = form.save(commit=False)
            new_kit.user = request.user
            new_kit.save()
            return http.HttpResponseRedirect(reverse('medikit:edit_kits'))
    else:
        form = AddKitForm()

    items = Kit.objects.filter(user__id=request.user.id)

    context = {
        'form': form,
        'items': items,
    }

    return render(request, 'medikit/edit_kits.html', context)


@login_required
def remove_kit(request, kit_id):
    kit = get_object_or_404(Kit, id=kit_id)
    kit.delete()

    return redirect('medikit:edit_kits')


@login_required
def edit_medications(request):
    if request.method == 'POST':
        form = AddMedicationForm(user_id=request.user.id, data=request.POST)
        if form.is_valid():
            form.save()
            return http.HttpResponseRedirect(reverse('medikit:edit_medications'))
    else:
        form = AddMedicationForm(user_id=request.user.id)

    current_user_kits = Kit.objects.filter(user__id=request.user.id)
    items = Medication.objects.filter(kit__in=current_user_kits)

    context = {
        'form': form,
        'items': items,
    }

    return render(request, 'medikit/edit_medications.html', context)


@login_required
def remove_medication(request, medication_id):
    medication = get_object_or_404(Medication, id=medication_id)
    medication.delete()

    return redirect('medikit:edit_medications')


def edit(request, item_type):
    users_kits = Kit.objects.filter(user__id=request.user.id)

    item_types = {
        'kit': {
            'form': AddKitForm,
            'items': users_kits
        },
        'drug': {
            'form': AddMedicationForm,
            'items': Medication.objects.filter(kit__in=users_kits)
        },
    }

    if request.method == 'POST':
        form = item_types[item_type]['form'](user_id=request.user.id, data=request.POST)
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
            'form': AddMedicationForm,
            'class': Medication,
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
