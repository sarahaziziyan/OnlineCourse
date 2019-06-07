from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import CustomUser


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password',)



class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('nationalCode',)