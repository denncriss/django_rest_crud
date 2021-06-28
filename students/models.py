from django.db import models
from courses.models import Course


class Student (models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_birth = models.DateField()
    email = models.CharField(max_length=50)

    course = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name
