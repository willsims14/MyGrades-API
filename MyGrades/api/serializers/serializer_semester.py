from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Semester


class SemesterSerializer(serializers.ModelSerializer):


    id = serializers.IntegerField(read_only=True)
    season = serializers.CharField()
    year = serializers.CharField()


    class Meta:
        model = Semester
        fields = ['id', 'season', 'year']

