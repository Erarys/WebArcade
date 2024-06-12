from django import forms
from django.contrib.auth.forms import UserCreationForm

from mailauth.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email"]
        field_classes = {"email": forms.EmailField}


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name"]
