from django import forms
from django.forms import ModelForm
from .models import CustomUser


class CustomUserChangeForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
        # fields = ('user.first_name', 'user.last_name', 'user.username', 'user.email', 'nationalCode')