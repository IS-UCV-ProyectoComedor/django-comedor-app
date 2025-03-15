from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegistrationStep1Form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['id_number', 'first_name', 'last_name', 'email', 'faculty', 'is_employee']

class UserRegistrationStep2Form(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['password1', 'password2']

class CustomLoginForm(forms.Form):
    id_number = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)