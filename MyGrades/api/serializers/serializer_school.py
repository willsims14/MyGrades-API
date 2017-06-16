from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import School


class SchoolSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = School
        exclude = ()


