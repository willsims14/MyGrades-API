from api.models import Student
from api.serializers import StudentSerializer

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response


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


class GetStudentByTokenView(APIView):
    def get(self, request, token, format=None):
        print("\n\nToken: {}\n\n".format(token))
        try:
            token_obj = Token.objects.get(pk=token)
            user = User.objects.get(pk=token_obj.user.id)
            serializer = StudentSerializer(user.student)
            return Response(serializer.data)
        except Token.DoesNotExist:
            raise Http404