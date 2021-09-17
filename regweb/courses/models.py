from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course (models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=60)
    semester = models.IntegerField()
    year = models.IntegerField()
    quota = models.IntegerField()
    student = models.ManyToManyField(User, blank=True,related_name = "user")
    status = models.BooleanField(default=True)
    

    def __str__(self):
        if self.quota == self.student.all().count :
            return f"{self.id} {self.code} : {self.name}: {self.semester}/{self.year}:{self.quota}:[CLOSE]"
        return f"{self.id} {self.code} : {self.name}: {self.semester}/{self.year}:{self.quota}:[OPEN]"
            
            