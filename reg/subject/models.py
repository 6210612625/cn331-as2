from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_id = models.CharField(max_length = 5)
    subject_name = models.CharField(max_length = 60 )
    
    def __str__(self):
        return f"{self.id}:{self.subject_id} :{self.subject_name}"
    

