from api.serializers import StudentCourseSerializer, StudentCourseSerializer, StudentCourseAssignmentSerializer
from api.models import StudentCourse, StudentCourse, StudentCourseAssignment, Course

from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status



class CourseList(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer

class CourseDetail(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer


# Get loggin in student's courses
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
