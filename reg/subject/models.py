from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Subject(models.Model):
    subject_id = models.CharField(max_length = 5, primary_key = True)
    subject_name = models.CharField(max_length=60)
    subject_semester = models.IntegerField()
    subject_year = models.IntegerField()
    subject_quota = models.IntegerField()
    student = models.ManyToManyField(User, blank=True, related_name="subject")

    def __str__ (self):
        return f"{self.subject_id} :{self.subject_name}"


