from api.serializers import *
from api.models import *

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json


class CourseView(APIView):
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        
        req_body = json.loads(request.body.decode())

        ###############################################
        ###############################################
        ## IF PROFESSOR INSTANCE EXISTS GRAB THAT #####
        ###############################################
        ###############################################
        # temp_professor = Professor.objects.get(name=req_body.professor)

        # if temp_professor:
        #       get_professor()
        # else:

        #     new_professor = Professor.objects.create(
        #         name = req_body['professor'],
        #         school = '',
        #         email = ''
        #     )


        semester_from_db = Semester.objects.get(pk=req_body['semester'])

        new_course = Course.objects.create(
            title = req_body['title'],
            course_number = req_body['course_number'],
            professor = req_body['professor'],
        )

        new_student_course = StudentCourse.objects.create(
            student = request.user.student,
            course = new_course,
            semester = semester_from_db
        )

        token = Token.objects.get(user=request.user)
        data = json.dumps({'token':token.key})

        try:
            new_course.save()
            new_student_course.save()
            return Response(data, content_type='application/json')
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
