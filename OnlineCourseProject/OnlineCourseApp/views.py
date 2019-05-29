from django.http import HttpResponse
from django.shortcuts import render

from .models import CustomUser
from django.contrib.auth.models import User


def login(request):
    return render(request, "login.html", {})


def sign_up(request):
    user_ins = User(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        username=request.POST['username'],
        password=request.POST['password'],
    )
    user_ins.save()
    custom_user_ins = CustomUser(
        user=User.objects.get(username=request.POST['username']),
        nationalCode=request.POST['national_code'],
    )
    custom_user_ins.save()
    return render(request, "dashboard.html", {});