from django import forms
from .models import Kit, Medication


class AddKitForm(forms.ModelForm):
    class Meta:
        model = Kit
        fields = ('name', )


class AddMedicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) or kwargs['instance'].kit.user
        super(AddMedicationForm, self).__init__(*args, **kwargs)
        self.fields['kit'].queryset = Kit.objects.filter(user__id=user.id)

    class Meta:
        model = Medication
        fields = ('name', 'description', 'expiration_date', 'kit')
