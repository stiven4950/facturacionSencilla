from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido",
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "El email ya está registrado, prueba con otro.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'name', 'lastname','phone', 'identity', 'address')
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'identity': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        help_text="Requerido, 254 caracteres como máximo y debe ser válido"
    )
    
    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if 'email' in self.cleaned_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "El email ya está registrado, prueba con otro.")
        return email

