from django.contrib.auth.models import User
from django.db import models
from django.db.models import *
from django.utils.timezone import now


class Category(Model):
    categoryId = CharField(max_length=10, primary_key=True)
    title = CharField(max_length=128)

    def __str__(self):
        return self.title


class Course(Model):
    courseId = CharField(max_length=10, primary_key=True)
    title = CharField(max_length=128)
    price = FloatField()
    image = ImageField(upload_to='course')
    creation_date = DateField(default=now)
    category = ForeignKey(Category, on_delete=CASCADE)

    def __str__(self):
        return self.title


class CustomUser(Model):
    user = models.OneToOneField(User, on_delete=PROTECT)
    nationalCode = CharField(max_length=10, primary_key=True)
    date_signup = DateField(default=now)

    def __str__(self):
        return self.user.first_name + self.user.last_name


class Instructor(Model):
    CustomUser = models.OneToOneField(CustomUser, on_delete=CASCADE)
    rank = IntegerField()
    last_education_level = CharField(max_length=8,
                           choices=[
                               ['Diploma','Diploma'],
                               ['Bachelor','Bachelor'],
                               ['Master','Master'],
                               ['PhD','PhD']
                           ])
    last_education_university = CharField(max_length=50)
    Course = ManyToManyField(Course, through='InstructorCourse')

    # def __str__(self):
    #     return 'Instructor' + super.__str__()


class InstructorCourse(Model):
    Instructor = ForeignKey(Instructor, on_delete=PROTECT)
    Course = ForeignKey(Course, on_delete=PROTECT)
    creation_date = DateField(default=now)


class Student(Model):
    CustomUser = models.OneToOneField(CustomUser, on_delete=CASCADE)
    pocket_money = FloatField()
    Course = ManyToManyField(Course, through='StudentCourse')

    # def __str__(self):
    #     return 'Student' + super.__str__()


class StudentCourse(Model):
    date_registration = DateField(default=now)
    Student = ForeignKey(Student, on_delete=PROTECT)
    Course = ForeignKey(Course, on_delete=PROTECT)