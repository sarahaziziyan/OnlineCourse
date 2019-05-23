from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import *

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Users)
admin.site.register(Instructor)
admin.site.register(InstructorCourse)
