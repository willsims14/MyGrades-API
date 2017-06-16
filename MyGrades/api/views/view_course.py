from api.models import Course
from api.serializers import CourseSerializer
from rest_framework import viewsets

class CourseList(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



