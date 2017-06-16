from api.models import StudentCourse
from api.serializers import StudentCourseSerializer
from rest_framework import viewsets

class CourseList(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer

class CourseDetail(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer
