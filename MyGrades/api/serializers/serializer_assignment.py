from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    course = serializers.CharField(source='course.title', read_only=True)
    # assignments = serializers.CharField(source='studentcourse.assignment.title', read_only=True)


    class Meta:
        model = Assignment
        exclude = ('url',)


