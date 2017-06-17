from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Student, StudentCourse


class StudentSerializer(serializers.HyperlinkedModelSerializer):


    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'school']


class AdminStudentSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Student
        exclude = ()

