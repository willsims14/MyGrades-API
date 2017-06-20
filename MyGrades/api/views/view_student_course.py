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

# Get logged in student's course's assignments
class StudentCourseAssignmentsViewSet(generics.ListAPIView):
    serializer_class = StudentCourseAssignmentSerializer
    model = StudentCourseAssignment

    def get_queryset(self):
        queryset = StudentCourseAssignment.objects.all()
        try:
            course_pk = float(self.request.query_params.get('course_id', None))
        except:
            student_courses = StudentCourse.objects.filter(student=self.request.user.student)
            queryset = StudentCourseAssignment.objects.filter(student_course__student=self.request.user.student)
            return queryset

        if course_pk is not None:
            queryset = StudentCourseAssignment.objects.filter(student_course=course_pk)

        return queryset




@api_view(['GET', 'PUT', 'DELETE'])
def DeleteCourseViewSet(request, pk):

    try:
        student_course = StudentCourse.objects.get(pk=pk)
    except StudentCourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # if request.method == 'GET':
    #     serializer = StudentCourseSerializer(product, context={'request': request})
    #     return Response(serializer.data)

    # elif request.method == 'PUT':
    #     serializer = ProductSerializer(product, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        course = Course.objects.get(pk=student_course.course.id)
        student_course.delete()

        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)