from django.contrib import admin

# Register your models here.
from .models import Subject

from .models import *

class SubjectAdmin(admin.ModelAdmin):
    list_display = ( "subject_id", "subject_name","subject_semester","subject_year","subject_quota")



admin.site.register(Subject, SubjectAdmin)
