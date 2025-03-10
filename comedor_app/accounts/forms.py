from django import forms # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from .models import CustomUser, UserCategory # type: ignore

class RegisterStep1Form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'faculty']

class RegisterStep2Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationStep1Form(forms.ModelForm):
    user_category = forms.ModelChoiceField(
        queryset=UserCategory.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['id_number', 'first_name', 'last_name', 'email', 'faculty', 'user_category']

class UserRegistrationStep2Form(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['password1', 'password2']

class CustomLoginForm(forms.Form):
    id_number = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class ManualUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    user_category = forms.ModelChoiceField(
        queryset=UserCategory.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['id_number', 'first_name', 'last_name', 'email', 'faculty', 'user_category']
        widgets = {
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'faculty': forms.TextInput(attrs={'class': 'form-control'}),
        }