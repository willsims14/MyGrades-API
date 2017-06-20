from api.serializers import *
from api.models import *

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json



class AssignmentView(APIView):
    # def get(self, request, pk, format=None):
    #     assignment = Assignment.objects.get(pk=pk)
    #     serializer = AssignmentSerializer(assignment, many=True)
    #     return Response(serializer.data)

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

        print("\n\n{}\n\n".format(temp_points_received))

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
