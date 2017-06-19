from django.db import models
from django.dispatch import receiver


class Semester(models.Model):
    """
    This class models a School in the API's database.

    ----Fields----


    Author: Will Sims
    """
    season = models.CharField(max_length=100)
    year = models.IntegerField(null=True)

    def __str__(self):
        return self.season

