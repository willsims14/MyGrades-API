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

        # Get instances of objects using foreign keys
        # product_type_pk = int(req_body['product_type'][0]);
        # product_type = ProductType.objects.get(pk=product_type_pk)

        print("\n\nBody: {}\n\n".format(req_body))

        new_course = Course.objects.create(
            title = req_body['title'],
            course_number = req_body['course_number'],
            professor = req_body['professor'],
        )

        token = Token.objects.get(user=request.user)
        print("\n\n\n{}\n\n".format(token.key))
        data = json.dumps({'token':token.key})
        print("\n\nData:{}\n\n".format(data))

        try:
            new_course.save()
            return Response(data, content_type='application/json')
        except:
            print('\n\nuh oh \n\n', new_course)
            return Response(status=status.HTTP_400_BAD_REQUEST)


    # Course ##################################
        # title = models.CharField(max_length=50)
        # course_number = models.CharField(max_length=50, blank=True, null=True)
        # professor = models.ForeignKey(Professor)

    # Student Course ##########################
        # student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_in_course')
        # course = models.ForeignKey(Course, on_delete=models.CASCADE)
        # assignments = models.ManyToManyField(Assignment, through='StudentCourseAssignment')