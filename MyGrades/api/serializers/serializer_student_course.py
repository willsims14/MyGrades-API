from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import StudentCourse
from api.serializers import StudentSerializer


class StudentCourseSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    course = serializers.CharField( read_only=True)
    description = serializers.CharField(read_only=True)
    semester = serializers.CharField(read_only=True)
    student = serializers.CharField(read_only=True)

    class Meta:
        model = StudentCourse
        exclude = ()


