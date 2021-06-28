from courses.models import Course
from rest_framework.viewsets import ModelViewSet
from courses.serializers import CoursesSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer

    def get_permissions(self):
        permissions = ''
        if self.request.method == 'GET':
            permissions = (AllowAny, )

        return [permission() for permission in permissions]
