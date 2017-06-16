from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from .model_school import School
from .model_course import Course
# from .model_student_course import StudentCourse


class Student(models.Model):
    """
    This class models a Student in the API's database.

    ----Fields----


    Author: Will Sims
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)



    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ('user',)



@receiver(post_save, sender=User)
def create_student_instance(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_student_instance(sender, instance, **kwargs):
    instance.student.save()
