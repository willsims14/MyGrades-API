from django.db import models
from django.contrib.auth.models import User
from .model_course import Course



class Assignment(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course)
    points_possible = models.DecimalField(max_digits=9, decimal_places=2)


    def __str__(self):
        return str(self.title)
