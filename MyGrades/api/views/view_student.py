from api.models import Student
from api.serializers import StudentSerializer

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response


# Retrieves user via username
class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get_queryset(self):
        queryset = Student.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset


# Retrieves student via authentication token
class GetStudentByTokenView(APIView):
    def get(self, request, token, format=None):
        try:
            token_obj = Token.objects.get(pk=token)
            user = User.objects.get(pk=token_obj.user.id)
            serializer = StudentSerializer(user.student)
            return Response(serializer.data)
        except Token.DoesNotExist:
            raise Http404