from api.models import Student, StudentCourse, StudentCourseAssignment
from api.serializers import StudentSerializer, AdminStudentSerializer, StudentCourseSerializer, StudentCourseAssignmentSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authtoken.models import Token
import json






class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# class StudentDetail(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer



# View Products within a certain product type
class StudentDetailViewSet(generics.ListAPIView):
    serializer_class = StudentSerializer
    model = Student

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Student.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset



class StudentCoursesViewSet(generics.ListAPIView):
    serializer_class = StudentCourseSerializer
    model = StudentCourse

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = StudentCourse.objects.all()
        pk = float(self.request.query_params.get('student_id', None))
        if pk is not None:
            queryset = StudentCourse.objects.filter(student=pk)

        return queryset

class StudentCourseAssignmentsViewSet(generics.ListAPIView):
    serializer_class = StudentCourseAssignmentSerializer
    model = StudentCourseAssignment

    def get_queryset(self):
        queryset = StudentCourseAssignment.objects.all()
        course_pk = float(self.request.query_params.get('course_id', None))
        if course_pk is not None:
            queryset = StudentCourseAssignment.objects.filter(student_course=course_pk)

        return queryset