from django.db import models
from django.dispatch import receiver


class School(models.Model):
    """
    This class models a School in the API's database.

    ----Fields----


    Author: Will Sims
    """
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.name

