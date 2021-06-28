from django.shortcuts import render
from students.models import Student
from students.serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
# Create your views here.


class StudentViewSet (ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        permissions = ''
        if self.request.method == 'GET':
            permissions = (AllowAny, )

        return [permission() for permission in permissions]
