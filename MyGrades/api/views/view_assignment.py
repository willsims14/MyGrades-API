from api.models import Assignment, StudentCourseAssignment
from api.serializers import AssignmentSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




class AssignmentList(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentDetail(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def DeleteAssignmentViewSet(request, pk):

    try:
        student_assignment = StudentCourseAssignment.objects.get(pk=pk)
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
        # course = Course.objects.get(pk=student_assignment.course.id)
        student_assignment.delete()
        student_assignment.assignment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)