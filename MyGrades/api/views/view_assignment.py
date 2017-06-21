from api.models import Assignment, StudentCourseAssignment, StudentCourse
from api.serializers import AssignmentSerializer, StudentCourseAssignmentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
import json


class AssignmentView(APIView):

    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


    def get_object(self):
        try:
            return StudentCourseAssignment.objects.filter(student_course__student=self.request.user.student)
        except StudentCourseAssignment.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        student_course_assignments = self.get_object()
        serializer = StudentCourseAssignmentSerializer(student_course_assignments, many=True)
        return Response(serializer.data)




    # def get_queryset(self):
    #     queryset = StudentCourseAssignment.objects.all()
    #     try:
    #         course_pk = float(self.request.query_params.get('course_id', None))
    #     except:
    #         student_courses = StudentCourse.objects.filter(student=self.request.user.student)
    #         queryset = StudentCourseAssignment.objects.filter(student_course__student=self.request.user.student)
    #         return queryset

    #     if course_pk is not None:
    #         queryset = StudentCourseAssignment.objects.filter(student_course=course_pk)

    #     return queryset

























    def post(self, request, student_course_pk, format=None):
        # Decode json
        req_body = json.loads(request.body.decode())

        # Get instances of objects
        student_course = StudentCourse.objects.get(course=student_course_pk)
        course = student_course.course

        # Create Assignment Object
        new_assignment = Assignment.objects.create(
            title = req_body['title'],
            course = course,
            points_possible = float(req_body['points_possible'])
        )

        try:
            temp_points_received = float(req_body['points_received'])
        except:
            temp_points_received = None

        # Create StudentCourseAssignment Object
        new_student_assignment = StudentCourseAssignment.objects.create(
            points_received = temp_points_received,
            description = req_body['description'],
            student_course = student_course,
            assignment = new_assignment
        )

        token = Token.objects.get(user=request.user)
        data = json.dumps({'token':token.key})

        try:
            new_assignment.save()
            new_student_assignment.save()
            return Response(data, content_type='application/json')
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            assignment = StudentCourseAssignment.objects.get(pk=pk)     # Get student assignment
            assignment.assignment.delete()                              # Delete Assignment instance attached to the StudentAssignment
            assignment.delete()                                         # Then delete the StudentAssignment
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
            

