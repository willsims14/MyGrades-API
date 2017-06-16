from django.db import models
from django.contrib.auth.models import User
from .model_school import School


class Professor(models.Model):
    """
    This class models a Student in the API's database.

    ----Fields----


    Author: Will Sims
    """

    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name
