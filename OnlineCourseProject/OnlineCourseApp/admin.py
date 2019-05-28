from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(CustomUser)
admin.site.register(Instructor)
admin.site.register(InstructorCourse)
admin.site.register(Student)
admin.site.register(StudentCourse)