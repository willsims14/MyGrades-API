from api.models import Assignment
from api.serializers import AssignmentSerializer
from rest_framework import viewsets

class AssignmentList(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentDetail(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
