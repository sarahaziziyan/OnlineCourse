from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm ,DateInput
from .models import CustomUser, Course

class MyDateInput(DateInput):
    input_type = 'date'

class CourseForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Course
        widgets = {'creation_date': MyDateInput()}


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password',)



class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('nationalCode',)