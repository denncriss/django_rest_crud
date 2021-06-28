from rest_framework.serializers import ModelSerializer
from courses.models import Course


class CoursesSerializer (ModelSerializer):
    class Meta:
        model: Course
        fields = ('name')
