from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import StudentCourseAssignment


class StudentCourseAssignmentSerializer(serializers.ModelSerializer):

    title = serializers.CharField(source="assignment.title", label='title')
    points_possible = serializers.CharField(source="assignment.points_possible")

    class Meta:
        model = StudentCourseAssignment
        fields = ['id', 'description','student_course', 'title','points_received', 'points_possible']

