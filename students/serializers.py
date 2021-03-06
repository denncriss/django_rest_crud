from rest_framework.serializers import ModelSerializer
from students.models import Student


class StudentSerializer (ModelSerializer):
    class Meta:
        model: Student
        fields = ('name', 'last_name', 'date_birth', 'email')
