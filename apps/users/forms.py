from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'profile_picture')

# Custom form for resetting password without email verification
class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(label="Seu Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label="Nova Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label="Confirme a nova senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        pw1 = cleaned_data.get("new_password1")
        pw2 = cleaned_data.get("new_password2")
        if pw1 and pw2 and pw1 != pw2:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data
