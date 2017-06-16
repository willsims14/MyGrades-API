from django.db import models
from django.contrib.auth.models import User
from api.models import Professor, StudentCourse, Assignment


class StudentCourseAssignment(models.Model):
    points_received = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.CharField(max_length=255)
    student_course = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.assignment.title)
