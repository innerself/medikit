from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddKitForm, AddMedicationForm, UserRegistrationForm
from .models import Kit, Medication


def home(request):
    if request.user.is_authenticated:
        context = {
            'kits': Kit.objects.filter(user__id=request.user.id),
        }
        return render(request, 'medikit/dashboard.html', context)
    else:
        return render(request, 'medikit/welcome.html', {})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            Kit.objects.create(name='Without kit', user=new_user)

            return render(request, 'medikit/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'medikit/register.html', {'user_form': user_form})


@login_required
def edit_kits(request):
    if request.method == 'POST':
        form = AddKitForm(data=request.POST)
        if form.is_valid():
            new_kit = form.save(commit=False)
            new_kit.user = request.user
            new_kit.save()
            return redirect('medikit:edit_kits')
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
            return redirect('medikit:edit_kits')
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
            return redirect('medikit:edit_medications')
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
            return redirect('medikit:edit_medications')
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
