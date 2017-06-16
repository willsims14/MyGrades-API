from api.models import Professor
from api.serializers import ProfessorSerializer
from rest_framework import viewsets

class ProfessorList(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer