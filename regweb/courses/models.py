from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course (models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=60)
    semester = models.IntegerField()
    year = models.IntegerField()
    quota = models.PositiveIntegerField(default =2)
    student = models.ManyToManyField(User, blank=True,related_name = "userses")
    status = models.BooleanField(default=True)


    def __str__(self):
        if (self.quota == self.student.all().count() ) or (self.status == False):
            return f"{self.id}. {self.code} : {self.name} semester: {self.semester}/{self.year} seats:{self.student.all().count()}/{self.quota}:[CLOSE]"
        return f"{self.id}. {self.code} : {self.name} semester: {self.semester}/{self.year} seats:{self.student.all().count()}/{self.quota}:[OPEN]"

    def is_seat_available(self):
        return self.student.count() < self.quota
        