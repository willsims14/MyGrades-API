from api.serializers import SemesterSerializer
from api.models import Semester

from rest_framework import generics
from rest_framework.response import Response



# Get Student on Login
class SemesterViewSet(generics.ListAPIView):
    serializer_class = SemesterSerializer
    model = Semester

    def get_queryset(self):
        queryset = Semester.objects.all()
        if queryset is not None:
            return queryset
