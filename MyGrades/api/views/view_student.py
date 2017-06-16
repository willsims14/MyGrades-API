from api.models import Student, StudentCourse
from api.serializers import StudentSerializer, AdminStudentSerializer, StudentCourseSerializer
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


# @api_view(['GET', 'PUT', 'DELETE'])
# def ProductDetailViewSet(request, student_id):
#         try:
#             courses = StudentCourse.objects.all()
#             print("\n\n{}\n\n".format(courses))
#         except StudentCourse.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         if request.method == 'GET':
#             courses = courses.filter(student=student_id)
#             serializer = StudentCourseSerializer(courses, context={'request': request})
#             return Response(serializer.data)

#         elif request.method == 'PUT':
#             serializer = StudentCourseSerializer(courses, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         elif request.method == "DELETE":
#             print("\n\n\n\nDELETEING\n\n\n\n\n")
#             courses.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)