from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import StudentCourse
from .serializer_assignment import AssignmentSerializer


class StudentCourseSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    course = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = StudentCourse
        exclude = ()


