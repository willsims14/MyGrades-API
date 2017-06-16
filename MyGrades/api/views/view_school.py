from api.models import School
from api.serializers import SchoolSerializer
from rest_framework import viewsets

class SchoolList(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer