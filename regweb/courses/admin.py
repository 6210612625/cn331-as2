from django.contrib import admin

# Register your models here.

from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ( "id","code","name","semester","year","quota","status")

admin.site.register(Course, CourseAdmin)
