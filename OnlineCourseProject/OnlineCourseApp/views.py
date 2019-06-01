from django.core.paginator import Paginator
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
        user=user_ins,
        nationalCode=request.POST['national_code'],
    )
    custom_user_ins.save()
    return render(request, "dashboard.html", {});


def listing(requset):
    contactList = CustomUser.objects.all()
    paginator  = Paginator(contactList, 2)
    page = requset.GET.get('page' , 1)
    return render(requset, 'dashboard.html', {'contacts',contactList})