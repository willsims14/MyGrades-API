from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        exclude = ()