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
def edit_kit(request, kit_id):
    kit = get_object_or_404(Kit, id=kit_id)
    if request.method == 'POST':
        form = AddKitForm(instance=kit, data=request.POST)
        if form.is_valid():
            form.save()
            return http.HttpResponseRedirect(reverse('medikit:edit_kits'))
    else:
        form = AddKitForm(instance=kit)

    context = {
        'form': form,
    }

    return render(request, 'medikit/edit_kit.html', context)


@login_required
def remove_kit(request, kit_id):
    kit = get_object_or_404(Kit, id=kit_id)
    kit.delete()

    return redirect('medikit:edit_kits')


@login_required
def edit_medications(request):
    if request.method == 'POST':
        form = AddMedicationForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return http.HttpResponseRedirect(reverse('medikit:edit_medications'))
    else:
        form = AddMedicationForm(user=request.user)

    kits = Kit.objects.filter(user__id=request.user.id)

    context = {
        'form': form,
        'kits': kits,
    }

    return render(request, 'medikit/edit_medications.html', context)


@login_required
def edit_medication(request, medication_id):
    medication = get_object_or_404(Medication, id=medication_id)
    if request.method == 'POST':
        form = AddMedicationForm(instance=medication, data=request.POST)
        if form.is_valid():
            form.save()
            return http.HttpResponseRedirect(reverse('medikit:edit_medications'))
    else:
        form = AddMedicationForm(instance=medication)

    context = {
        'form': form,
    }

    return render(request, 'medikit/edit_medication.html', context)


@login_required
def remove_medication(request, medication_id):
    medication = get_object_or_404(Medication, id=medication_id)
    medication.delete()

    return redirect('medikit:edit_medications')
