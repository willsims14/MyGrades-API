from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import StudentCourseAssignment


class StudentCourseAssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentCourseAssignment
        exclude = ()


