from api.models import Student
from api.serializers import StudentSerializer

from rest_framework import viewsets
from rest_framework import generics


class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Get Student on Login
class StudentDetailViewSet(generics.ListAPIView):
    serializer_class = StudentSerializer
    model = Student


    def get_queryset(self):
        queryset = Student.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset

