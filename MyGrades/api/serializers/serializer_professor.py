from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Professor


class ProfessorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professor
        exclude = ()