from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import StudentCourse
from .serializer_student_course_assignment import StudentCourseAssignmentSerializer


class StudentCourseSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    course = serializers.CharField(source='course.title', read_only=True)
    description = serializers.CharField(read_only=True)
    # assignments = StudentCourseAssignmentSerializer(many=True)

    class Meta:
        model = StudentCourse
        exclude = ()


