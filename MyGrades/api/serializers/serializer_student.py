from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Student, StudentCourse


class StudentSerializer(serializers.HyperlinkedModelSerializer):


    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Student
        exclude = ('url', 'user',)


class AdminStudentSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Student
        exclude = ()

