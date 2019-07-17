import datetime
import json
from encodings.utf_8 import encode

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf

from .forms import *
from .models import CustomUser, Course, Instructor, Student
from django.contrib.auth.models import User


def giveCoursesPage(request,coursesList):
    paginator = Paginator(coursesList, 3)
    page = request.GET.get('page', 1)
    courses = paginator.get_page(page)
    return render(request, 'index.html', {'courses': courses})


def index(request):
    coursesList = Course.objects.all()
    return giveCoursesPage(request,coursesList)


def index_premade(request):
    return render(request, "index_premade.html", {})


def search_courses(request):
    title = request.POST.get('searchCourseInput', '')
    coursesList = Course.objects.filter(title__contains=title)
    return giveCoursesPage(request, coursesList)

def remove_search_courses(request):
    return index(request)

def myLogin(request):
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
            coursesList = Course.objects.all()
            args = {}
            args.update(csrf(request))
            args['username'] = username
            args['courses'] = coursesList
            login(request, user)
            request.session['lastLoginTime'] = str(datetime.datetime.now())
            request.session['electronicWallet'] = 100000
            return render(request, "index.html", args)
    else:
        return render(request, "login.html", {})

def sign_up(request):
    password2 = request.POST['password_confirm']
    password = request.POST['password']
    if password == password2:
        email = request.POST['email']
        username = request.POST['username']
        userType = request.POST['userType']
        new_user = User.objects.create_user(username=username, email=email, password=password)
        custom_user_ins = CustomUser(
            user=User.objects.get(username=request.POST['username']),
            userType=userType,
        )
        custom_user_ins.save()
        if userType=="instructor":
            instructor_ins = Instructor.objects.create(customUser=custom_user_ins,rank=0)
            instructor_ins.save()
        else:
            student_ins = Student.objects.create(customUser=custom_user_ins,pocket_money=0)
            student_ins.save()

        args = {}
        args.update(csrf(request))
        args['errorMsg'] = 'لطفا وارد شوید'
        return render(request, "login.html", args);
    else:
        return render(request, "login.html", {'errorMsg': 'پسورد و تکرار آن متفاوت هستند'});


def logout(request):
    return render(request, "login.html", {'errorMsg': 'لطفا وارد شوید'})


def edit_profile(request):
    print(request.user)
    print(request.user.username)
    userForm = UserForm()
    customUserForm = CustomUserForm()
    if request.user.is_authenticated:
        return render(request, "editProfile.html", {'userForm':userForm , 'form':customUserForm})
    else:
        return render(request, "login.html", {'errorMsg': 'لطفا وارد شوید'})


def update_profile_data(requset):
    return HttpResponse('yes')


def bootstrapDemo(request):
    userForm = UserForm();
    return render(request, "bootstrapDemo.html",{'form':userForm})


# def search_courses(request):
#     if request.user.is_authenticated:
#         coursesList = Course.objects.all()
#         paginator  = Paginator(coursesList, 5)
#         page = request.GET.get('page' , 1)
#         courses = paginator.get_page(page)
#         return render(request, 'search_courses.html', {'courses': courses})
#     else:
#         return render(request, "login.html", {'errorMsg': 'لطفا وارد شوید'})

def my_courses(request):
    pass


# def listing(requset):
#     contactList = CustomUser.objects.all()
#     paginator  = Paginator(contactList, 2)
#     page = requset.GET.get('page' , 1)
#     return render(requset, 'dashboard.html', {'contacts',contactList})