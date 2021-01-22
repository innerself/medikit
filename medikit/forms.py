from django import forms
from .models import Kit, Drug


class AddKitForm(forms.ModelForm):
    class Meta:
        model = Kit
        fields = ('name', )


class AddDrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ('name', 'description', 'expiration_date', 'kit')
