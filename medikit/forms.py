from django import forms
from django.contrib.auth import get_user_model

from .models import Kit, Medication


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')

        return cd['password']


class AddKitForm(forms.ModelForm):
    class Meta:
        model = Kit
        fields = ('name', )


class AddMedicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) or kwargs['instance'].kit.user
        super(AddMedicationForm, self).__init__(*args, **kwargs)
        self.fields['kit'].queryset = Kit.objects.filter(
            user__id=user.id
        ).order_by(
            'name'
        )

    class Meta:
        model = Medication
        fields = ('name', 'description', 'expiration_date', 'kit')
        widgets = {
            'expiration_date': forms.SelectDateWidget,
        }
