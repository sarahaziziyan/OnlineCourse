from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

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
            return render(request, "dashboard.html", {})
    else:
        return render(request, "login.html", {})


def sign_up(request):
    u = UserCreationForm(request.POST)
    UserCreationForm.
    if u.is_valid():
        u.save()
        # return HttpResponse('Done')
        return render(request, "login.html", {'errorMsg': 'لطفا وارد شوید'});
    else:
        #return HttpResponse('Error')
        return render(request, "login.html", {'errorMsg': 'عملیات ثبت کاربر با خطا مواجه شد'});
    # user_ins = User(
    #     email=request.POST['email'],
    #     username=request.POST['username'],
    #     password=request.POST['password'],
    # )
    # user_ins.save()
    # return render(request, "login.html", {'errorMsg':'لطفا وارد شوید'});


# def listing(requset):
#     contactList = CustomUser.objects.all()
#     paginator  = Paginator(contactList, 2)
#     page = requset.GET.get('page' , 1)
#     return render(requset, 'dashboard.html', {'contacts',contactList})