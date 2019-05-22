from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    categoryId = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Course(models.Model):
    courseId = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=128)
    price = models.IntegerField()
    image = models.ImageField(upload_to='course')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Users(models.Model):
    nationalCode = models.CharField(max_length=10, primary_key=True)
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)
    email = models.CharField(max_length=128)


class Instructor(Users):
    Course = models.ManyToManyField(Course, through='InstructorCourse')


class InstructorCourse(models.Model):
    Instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT)
    Course = models.ForeignKey(Course, on_delete=models.PROTECT)
    creation_date = models.DateField(default=now())
