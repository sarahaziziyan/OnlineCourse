from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from .forms import *
from .models import CustomUser
from django.contrib.auth.models import User


def login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)
    print(username)
    print(password)
    print(user)
    if request.POST:
        if user is None:
            return render(request, "login.html", {'errorMsg':'نام کاربری یا کلمه عبور اشتباه است'} )
        else:
            return render(request, "dashboard.html", {'firstname':user.first_name , 'lastname':user.last_name})
    else:
        return render(request, "login.html", {})


def sign_up(request):
    password2 = request.POST['password_confirm']
    password = request.POST['password']
    if password == password2:
        email = request.POST['email']
        username = request.POST['username']
        new_user = User.objects.create_user(username=username, email=email, password=password)
        return render(request, "login.html", {'errorMsg':'لطفا وارد شوید'});
    else:
        return render(request, "login.html", {'errorMsg': 'پسورد و تکرار آن متفاوت هستند'});


def logout(request):
    return render(request, "login.html", {'errorMsg': 'لطفا وارد شوید'});


def edit_profile(request):
    userForm = UserForm();
    customUserForm = CustomUserForm();
    if request.user.is_authenticated:
        return render(request, "editProfile.html", {'userForm':userForm , 'customUserForm':customUserForm});
    else:
        return render(request, "login.html", {'errorMsg': 'لطفا وارد شوید'});

def update_profile_data(requset):
    return HttpResponse('yes')

# def listing(requset):
#     contactList = CustomUser.objects.all()
#     paginator  = Paginator(contactList, 2)
#     page = requset.GET.get('page' , 1)
#     return render(requset, 'dashboard.html', {'contacts',contactList})