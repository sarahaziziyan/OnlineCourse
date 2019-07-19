import datetime
import json
from encodings.utf_8 import encode

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf

from .forms import *
from .models import CustomUser, Course, Instructor, Student
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *


def giveCoursesPage(request,coursesList, args):
    paginator = Paginator(coursesList, 3)
    page = request.GET.get('page', 1)
    courses = paginator.get_page(page)
    args['courses'] = coursesList
    return render(request, 'index.html', args)


def index(request):
    coursesList = Course.objects.all()
    args = {}
    args.update(csrf(request))
    args['username'] = None
    args['userType'] = None
    return giveCoursesPage(request, coursesList, args)


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
            return render(request, "login.html", {'errorMsg':'Username or password is wrong'} )
        else:
            customUserType = CustomUser.objects.get(user=user).userType
            coursesList = Course.objects.all()
            args = {}
            args.update(csrf(request))
            args['username'] = username
            args['userType'] = customUserType
            args['courses'] = coursesList
            login(request, user)
            request.session['lastLoginTime'] = str(datetime.datetime.now())
            request.session['electronicWallet'] = 100000
            request.session['userType'] = customUserType
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
            instructor_ins = Instructor.objects.create(customUser=CustomUser.objects.get(user=custom_user_ins.user),rank=0)
            instructor_ins.save()
        else:
            student_ins = Student.objects.create(customUser=CustomUser.objects.get(user=custom_user_ins.user),pocket_money=0)
            student_ins.save()

        args = {}
        args.update(csrf(request))
        args['errorMsg'] = 'Please login'
        return render(request, "login.html", args);
    else:
        return render(request, "login.html", {'errorMsg': 'The password and repeat password are different'});


def logout(request):
    return render(request, "login.html", {'errorMsg': 'Please Login'})

def dashboard_course(request):
    pass

def create_course(request):
    userType = request.session.get('userType', None)
    if request.user.is_authenticated:
        if userType == 'instructor':
            return render(request, 'create_courses.html' , {'title': 'Create Course','form': CourseForm()})
        else:
            return render(request, "login.html", {'errorMsg': 'Please login as an instructor'})
    else:
        return render(request, "login.html", {'errorMsg': 'Please login'})

def save_course(request):
    pass


def edit_profile(request):
    print(request.user)
    print(request.user.username)
    userForm = UserForm()
    customUserForm = CustomUserForm()
    if request.user.is_authenticated:
        return render(request, "editProfile.html", {'userForm':userForm , 'form':customUserForm})
    else:
        return render(request, "login.html", {'errorMsg': 'Please login'})


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