from django.db import models
from django.contrib.auth.models import User
from .model_professor import Professor



class Course(models.Model):
    title = models.CharField(max_length=50)
    course_number = models.CharField(max_length=50, blank=True, null=True)
    professor = models.CharField(max_length=50, blank=True, null=True)
    # professor = models.ForeignKey(Professor)


    def __str__(self):
        return str(self.title)
