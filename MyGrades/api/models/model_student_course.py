from django.db import models
from django.contrib.auth.models import User
from .model_student import Student
from .model_course import Course
from .model_assignment import Assignment
from .model_semester import Semester


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_in_course')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignments = models.ManyToManyField(Assignment, through='StudentCourseAssignment')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.student.user.first_name + ": " + self.course.title

